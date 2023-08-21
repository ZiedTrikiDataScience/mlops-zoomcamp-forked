import datetime
import time
import random
import logging 
import uuid
import pytz
import pandas as pd
import io
import psycopg

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s]: %(message)s")

SEND_TIMEOUT = 10
rand = random.Random()

Create_Table_Statement = """
DROP TABLE IF EXISTS Dummy_Metrics_MLOps;
CREATE TABLE Dummy_Metrics_MLOps (
	Timestamp_Of_The_Detection timestamp,
	Value1 integer,
	Value2 varchar,
	Value3 float
)
"""

def prep_db():
	with psycopg.connect("host=localhost port=5432 user=postgres password=example", autocommit=True) as conn:
		res = conn.execute("SELECT 1 FROM pg_database WHERE datname='test'")
  
		if len(res.fetchall()) == 0:
			conn.execute("CREATE DATABASE test;")
		logging.info("Database Successefuly Created")
   
		with psycopg.connect("host=localhost port=5432 dbname=test user=postgres password=example") as conn:
			conn.execute(Create_Table_Statement)
		logging.info("Table Dummy_Metrics_MLOps Successefuly Created")
   
   

def calculate_dummy_metrics_postgresql(curr):
	value1 = rand.randint(0, 1000)
	value2 = str(uuid.uuid4())
	value3 = rand.random()

	curr.execute(
		"INSERT INTO Dummy_Metrics_MLOps(Timestamp_Of_The_Detection, Value1, Value2, Value3) values (%s, %s, %s, %s)",
		(datetime.datetime.now(pytz.timezone('Europe/London')), value1, value2, value3)
	)
	logging.info("Data Successefully Inserted")



def main():
	prep_db()
 
	last_send = datetime.datetime.now() - datetime.timedelta(seconds=10)
 
	with psycopg.connect("host=localhost port=5432 dbname=test user=postgres password=example", autocommit=True) as conn:
		for i in range(0, 100):
			with conn.cursor() as curr:
				calculate_dummy_metrics_postgresql(curr)
    

			new_send = datetime.datetime.now()
			seconds_elapsed = (new_send - last_send).total_seconds()
   
			if seconds_elapsed < SEND_TIMEOUT:
				time.sleep(SEND_TIMEOUT - seconds_elapsed)
    
			while last_send < new_send:
				last_send = last_send + datetime.timedelta(seconds=10)
			logging.info("The Data is Sent Successefuly")

if __name__ == '__main__':
	main()