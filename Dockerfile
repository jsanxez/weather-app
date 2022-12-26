FROM  python:3.10.9
RUN pip install fastapi uvicorn[standard] jinja2 requests python-multipart
COPY ./app /app
COPY ./templates /templates
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
