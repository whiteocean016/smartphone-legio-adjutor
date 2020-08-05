FROM python:3.6

EXPOSE 8050

WORKDIR /app/

ADD requirements.txt /app/
RUN pip install -r requirements.txt

ADD ./utils /app/utils
ADD app.py /app/

RUN mkdir /app/data

CMD [ "python3", "app.py" ]