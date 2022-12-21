FROM python:latest
Workdir /app
Copy . .
Run pip install -r requirements.txt
Entrypoint ["python"]
Cmd ["app.py"]