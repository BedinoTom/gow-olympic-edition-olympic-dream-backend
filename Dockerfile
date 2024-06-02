FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./gow /code/gow

CMD ["uvicorn", "gow.main:app", "--host", "0.0.0.0", "--port", "80"]