sleep 30s
/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P password -Q 'CREATE DATABASE [dabase]'
/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P password -d 'dabase' -i /src/create-db.sql

