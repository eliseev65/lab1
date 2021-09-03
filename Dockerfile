FROM python:3

COPY script.py /script.py

RUN chmod +x /script.py

CMD python3 /script.py