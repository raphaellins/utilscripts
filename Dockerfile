# FROM mcr.microsoft.com/mssql/server:2017-CU11-ubuntu
FROM mcr.microsoft.com/mssql/server:2017-latest-ubuntu

# COPY ./create-db.sql .

WORKDIR /
COPY ./initialize.sh /src/
COPY ./create-db.sql /src/

ENV ACCEPT_EULA Y

ENV SA_PASSWORD PASSWORD

ENV MSSQL_PID Express

RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc

RUN chmod +x /src/initialize.sh

RUN ( /opt/mssql/bin/sqlservr --accept-eula & ) | grep -q "Service Broker manager has started" \
    && /src/initialize.sh

# 1 > docker build -t db-demo .
# 2 > docker run -p 1433:1433 -d db-demo