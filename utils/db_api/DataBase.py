import sqlite3
import datetime

db = sqlite3.connect('client_users.db', check_same_thread=False)
sql = db.cursor()