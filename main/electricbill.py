import sqlite3
from cbill import bill

conn=sqlite3.connect('electric_bill.db')

c=conn.cursor()