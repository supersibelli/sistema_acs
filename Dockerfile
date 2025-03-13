FROM python:3.8-slim

WORKDIR /app

COPY requirements/prod.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "run:app", "-b", "0.0.0.0:5000"] 