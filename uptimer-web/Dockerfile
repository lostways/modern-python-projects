FROM python:3.10.1-buster

# Copy requirements to container. Docker will chache the output of
# any command that uses this file unless the contents have changed.
COPY requirements.txt .
RUN pip install -r requirements.txt

# Create new user, move to user's home dir, switch to new user
RUN useradd --create-home --shell /bin/bash app
WORKDIR /home/app
USER app

# Open port 8000
EXPOSE 8000

# Copy code to container
COPY . .

# Start app with gunicorn
ENTRYPOINT [ "gunicorn", "-w", "3", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000", "main:app" ]