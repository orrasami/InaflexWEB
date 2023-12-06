FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
EXPOSE 8000
