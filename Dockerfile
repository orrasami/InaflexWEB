FROM python:3.9-slim
WORKDIR /app
COPY . /app

docker run --name some-postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


EXPOSE 80

CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]


# Base image
FROM python:3.9-slim

# Working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Expose the server port
EXPOSE 8000

# Command to start the server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "inaflex.wsgi"]