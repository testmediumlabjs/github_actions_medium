FROM python:3.7.9-alpine
COPY ./app /app
RUN pip3 install -r ./app/requirements.txt
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "15400"]