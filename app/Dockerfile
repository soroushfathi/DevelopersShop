FROM python:3.9-alpine

# setup env var
ENV HOME=/home/app/webapp

RUN mkdir -p $HOME

WORKDIR ${HOME}

RUN pip install --upgrade pip

COPY . $HOME

EXPOSE 8000

RUN pip install -r requirements.txt

CMD python manage.py runserver
