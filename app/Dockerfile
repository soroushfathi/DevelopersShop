FROM python:3.9-alpine

# setup env var
ENV HOME=/home

RUN mkdir -p $HOME

WORKDIR ${HOME}

RUN pip install --upgrade pip

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python",  "manage.py" ,"runserver", "0.0.0.0:8000"]
