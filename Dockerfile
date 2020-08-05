FROM python:3.6

EXPOSE 8050

WORKDIR /app/

ADD requirements.txt /app/
RUN pip install -r requirements.txt

ADD get_antutu.py /app/
ADD get_geekbench.py /app/
ADD get_gsmarena.py /app/
ADD get_passmark.py /app/
ADD get_latest_data.py /app/
ADD app.py /app/

RUN mkdir /app/data

CMD [ "python3", "app.py" ]