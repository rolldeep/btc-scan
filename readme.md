## BTC/UTC etl implementation
project for simple implementation of ETL to pull the data [from](https://exchangerate.host).

### SET-UP
1) install pipenv: \
`pip install pipenv`
2) run pipenv command: \
`pipenv install -r requirements.txt`
3) create directories for airflow: \
`mkdir data logs plugins`
4) create .env file: \
`echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env`
5) start airflow in localExecutor mode (it's going to take a while): \
`docker-compose up -d`


