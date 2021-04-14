FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV DISPLAY <IPADDRESS>:0
RUN apk add --no-cache gcc musl-dev linux-headers
RUN apk add --update docker openrc
RUN rc-update add docker boot
RUN apk add xterm
COPY main.html ./templates/main.html
RUN pip install flask
EXPOSE 5000
COPY . .
CMD ["flask", "run"]