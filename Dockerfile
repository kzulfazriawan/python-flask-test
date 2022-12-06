FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /project
COPY ./backend/requirements.txt /project/
RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt
COPY ./backend /project/