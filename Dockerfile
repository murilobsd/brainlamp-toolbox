FROM python:3.6.2-alpine3.6

RUN adduser -S brain_lamp
WORKDIR /home/brain_lamp/toolbox

COPY . .

RUN python setup.py develop
RUN python -c "import nltk ; nltk.download('punkt')"
RUN python -c "import nltk ; nltk.download('stopwords')"
