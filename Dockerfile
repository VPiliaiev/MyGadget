FROM python:3.12-rc-slim

RUN apt update
RUN mkdir /my_gadget

WORKDIR /my_gadget

COPY ./src ./src
COPY ./requirements.txt ./requirements.txt

RUN python -m pip install --upgrade & pip install -r ./requirements.txt
CMD ["python", "src/manage.py", "runserver", "8008"]
