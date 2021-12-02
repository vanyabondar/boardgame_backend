# syntax=docker/dockerfile:1
FROM python:3.8

# to see logs immediately
ENV PYTHONUNBUFFERED=1

WORKDIR /boardgame_backend
COPY . /boardgame_backend/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]