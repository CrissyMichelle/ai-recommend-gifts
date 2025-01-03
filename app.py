import os
from openai import AzureOpenAI
from dotenv import load_dotenv
from flask import Flask, render_template, request
from forms import GiftForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'red-jellyfish-night'

load_dotenv()

client = AzureOpenAI(
    azure_endpoint="https://ai-giftrecommender2025ai060225318907.openai.azure.com/openai/deployments/gpt-4o-mini/chat/completions?api-version=2024-08-01-preview",
    api_version="2024-08-01-preview",
    api_key=os.getenv("OPENAI_API_KEY")
)

def query_gpt3(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system",
                 "content":"You are a helpful gift-recommendations friend."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error querying GPT: {e}")
        return "I'm sorry, I seem to be having trouble with gift requests atm."

@app.route("/", methods=["GET", "POST"])
def index():
    form = GiftForm()
    gifts = None
    if form.validate_on_submit():
        prompt = (
            f"My loved one is {form.age.data} years old, "
            f"identifies as {form.gender.data}, "
            f"and has these hobbies: {form.hobby.data}. "
            f"When it comes to spending money I'm {form.budget.data}. "
            f"Please recommend thoughtful, creative, and unique gift ideas."
        )
        gifts = query_gpt3(prompt)
    return render_template("index.html", form=form, gifts=gifts)

@app.route("/refresh", methods=["GET"])
def refresh():
    return render_template("index.html", form=GiftForm(), gifts=None)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
