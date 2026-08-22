# JDBC driver

PySpark needs the Postgres JDBC driver to read/write the database. It's a
~1 MB binary file, not committed to this repo (see `.gitignore`).

Download it and put it here:

```bash
curl -L -o jars/postgresql-42.7.3.jar \
  https://jdbc.postgresql.org/download/postgresql-42.7.3.jar
```

That's it -- `settings.py` already points at this file by default.
