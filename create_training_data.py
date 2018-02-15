import sqlite3
import pandas as pd

timeframes = ['2008-04']

for timeframe in timeframes:
    connection = sqlite3.connect('{}'.db.format(timeframe))
    c = connection.cursor()
    limit = 5000