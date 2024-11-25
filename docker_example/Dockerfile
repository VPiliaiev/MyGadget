FROM python:3.11-rc-slim

RUN apt update & python --version
COPY ./hello_docker.py ./hello_docker.py
COPY ./requirements.txt ./requirements.txt

RUN python -m pip install --upgrade & pip install -r ./requirements.txt
CMD ["python", "./hello_docker.py"]
