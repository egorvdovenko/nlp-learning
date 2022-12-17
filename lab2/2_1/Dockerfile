FROM python:3.8-slim-buster
WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get install -y --no-install-recommends git

RUN pip install nltk
RUN pip install razdel
RUN pip install mosestokenizer
RUN pip install xlsxwriter 
RUN pip install git+https://github.com/Koziev/rutokenizer

CMD [ "python", "./lab2_1.py" ]