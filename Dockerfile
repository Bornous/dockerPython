FROM alpine:latest

#UPDATE
RUN apk add --update python py-pip

#Install app depencies
RUN pip install Flask

#Bundle app source
COPY simpleapp.py /src/simpleapp.py

EXPOSE 8000
CMD ["python", "/src/simpleapp.py", "-p 8000"]
