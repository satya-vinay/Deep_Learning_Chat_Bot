import sqlite3
import json
from datetime import datetime

timeFrame = '2006-01'
sql_transaction = []

connection = sqlite3.connect('{}.db'.format(timeFrame))
c = connection.cursor()

def create_table():                             #create Database for comemnts
    c.execute("""CREATE TABLE IF NOT EXISTS 
parent_reply(parent_id TEXT PRIMARY KEY, comment_id TEXT UNIQUE,parent TEXT,comment TEXT, subreddit TEXT,unix INT, score INT)""")



if __name__ == "__main__" :
    create_table()
    row_counter = 0
    paired_rows = 0             #number of parent and child pairs i.e comments and reply
