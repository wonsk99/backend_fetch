FROM python:3.12-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./fetch /code/fetch

CMD ["fastapi", "run", "fetch/main.py", "--port", "80"]
