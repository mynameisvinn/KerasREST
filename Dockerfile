FROM floydhub/dl-docker:cpu

COPY . /src
WORKDIR /src

RUN pip install flask
RUN pip install git+git://github.com/fchollet/keras.git --upgrade --no-deps
RUN pip install tensorflow --upgrade

ENTRYPOINT [ "python" ]

CMD [ "server.py" ]