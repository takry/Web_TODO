from python:3.8.6

RUN pip install --upgrade pip
COPY ./ ./
RUN pip3 install -r requirements.txt

RUN pip install gunicorn