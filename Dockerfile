FROM alpine:latest

#UPDATE
RUN apk add --update python3 py-pip

#Install app depencies
RUN pip3 install Flask

#Bundle app source
COPY simpleapp.py /src/simpleapp.py

EXPOSE 8000
CMD ["python3", "/src/simpleapp.py", "-p 8000"]
