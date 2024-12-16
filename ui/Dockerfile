FROM python:3

WORKDIR /usr/src/app


RUN pip install --no-cache-dir  streamlit

COPY . .
CMD [ "streamlit", "run","ui.py" ]
