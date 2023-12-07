FROM python:3.9
WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
