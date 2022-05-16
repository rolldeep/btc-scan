import pandas as pd
import requests
import pendulum
import json
from airflow.decorators import dag, task
from sqlalchemy import create_engine
from sqlalchemy.types import DECIMAL, DATETIME, VARCHAR

@dag(
    schedule_interval="0 */3 * * *",
    start_date=pendulum.datetime(2022, 1, 1, tz="UTC"),
    catchup=False,
    tags=["btc-usd"],
)
def get_currency_api_etl():
    """
    ### Getting the BTC/USD 
    [using](https://exchangerate.host)
    """

    @task()
    def extract():
        """Extract task"""
        
        url = "https://api.exchangerate.host/latest?base=USD"
        
        response = requests.get(url)
        data = response.json()

        return data

        


    @task()
    def transform_and_load(data: dict):
        """
        Transform task which takes in the API response,
        and ingest the data.
        """
        #transform
        df = pd.json_normalize(data)
        df = df[["date", "rates.BTC"]]
        df["pair"] = "USD/BTC"
        df.rename(columns={"rates.BTC": "rates"}, inplace=True)

        #ingest
        engine = create_engine(f"postgresql://postgres:admin@localhost:5433/postgres")
        dtype = {
            "date": DATETIME,
            "rates": DECIMAL,
            "pair": VARCHAR
        }
        df.to_sql(name="currency",con=engine, index=False, if_exists="append", dtype=dtype)

    order_data = extract()
    transform_and_load(order_data)



tutorial_etl_dag = get_currency_api_etl()
