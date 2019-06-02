FROM frolvlad/alpine-python3:latest

#UPDATE
RUN pip3 install --upgrade pip

#Install app depencies
RUN pip3 install Flask
RUN sudo apt install python3-pip
RUN sudo su
student
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN exit
RUN sudo apt-get UPDATE
RUN sudo ACCEPT_EULA=Y apt-get install msodbcsql17
RUN sudo apt install unixodbc-dev
RUN pip3 install --user pyodbc

#Bundle app source
COPY simpleapp.py /src/simpleapp.py

EXPOSE 8000
CMD ["python3", "/src/simpleapp.py", "-p 8000"]
