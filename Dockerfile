FROM python:3.9-slim

WORKDIR /app
COPY ./static /app/static/
COPY ./templates /app/templates/
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

CMD ["python", "-u", "app.py"]
