FROM  python:3.6.5-alpine

COPY requirements.txt /tmp/requirements.txt
RUN  pip install -r /tmp/requirements.txt

CMD ["pytest", "--junitxml", "results.xml", "/src/source/tests"]