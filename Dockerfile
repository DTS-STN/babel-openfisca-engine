FROM python:3-stretch
COPY . /openfisca
WORKDIR /openfisca

RUN pip install --upgrade pip && \
    pip install -e . && \
    #pip install -r requirements.txt
    pip install openfisca-canada_babel

EXPOSE 5000

CMD [ "/usr/local/bin/openfisca", "serve", "-b", "0.0.0.0:5000" ]
