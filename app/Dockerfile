FROM python:3.7.5-slim
RUN pip install --upgrade pip
RUN pip install flask==1.1.1
COPY ./src/app.py ./src/app.py
EXPOSE 80
CMD [ "python", "-u", "./src/app.py"]