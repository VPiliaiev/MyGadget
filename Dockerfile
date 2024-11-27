FROM python:3.12-rc-slim

RUN apt update
RUN mkdir /my_gadget

WORKDIR /my_gadget

COPY ./src ./src
COPY ./requirements.txt ./requirements.txt
COPY ./commands ./commands

RUN chmod +x /my_gadget/commands/start_server_dev.sh

RUN python -m pip install --upgrade & pip install -r ./requirements.txt

CMD ["/bin/sh"]

