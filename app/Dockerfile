FROM alpine

EXPOSE 5000

COPY key.pem cert.pem requirements.txt app.py ./

RUN apk add --no-cache py3-flask py3-pip

RUN pip install -r requirements.txt

CMD flask run --cert=cert.pem --key=key.pem --host=0.0.0.0