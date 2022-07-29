FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /fastapi_example

COPY ./requirements/prod.txt ./requirements/
COPY entrypoint.sh .

RUN pip3 install --upgrade pip -r ./requirements/prod.txt
RUN chmod +x entrypoint.sh

COPY ./ .

RUN chmod +x /fastapi_example//entrypoint.sh
ENTRYPOINT [ "/fastapi_example/entrypoint.sh" ]