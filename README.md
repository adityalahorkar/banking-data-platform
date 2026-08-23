# Banking Transaction Analytics Pipeline

An end-to-end data pipeline that loads a banking transactions dataset into PostgreSQL, transforms it with PySpark, models it into a star schema, and powers a Power BI dashboard. Processes 6.3M+ transaction rows.

## Architecture Diadram

<p align="center">
  <img src="docs/images/architecture_diagram.png" alt="Architecture" width="380">
</p>

## Tech stack

Python · PostgreSQL · PySpark · Apache Airflow (optional) · Power BI (optional)

## Project structure

```
├── settings.py          # config, loaded from .env
├── run_pipeline.py      # runs the full pipeline
├── pipeline/            # one file per step
├── sql/                 # schema + analytics views
├── airflow/             # optional scheduled orchestration
├── docs/                # architecture & data dictionary
├── tests/               # pytest tests
└── data/                # raw / processed / reports
```

## Setup

```bash
# 1. install dependencies
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 2. configure
cp .env.example .env            # add your Postgres password

# 3. download the JDBC driver
curl -L -o jars/postgresql-42.7.3.jar \
  https://jdbc.postgresql.org/download/postgresql-42.7.3.jar

# 4. add the dataset
# place transactions.csv in data/raw/

# 5. run everything
python run_pipeline.py
```

Dataset: [PaySim synthetic fraud detection dataset](https://www.kaggle.com/datasets/ealaxi/paysim1) (Kaggle).
