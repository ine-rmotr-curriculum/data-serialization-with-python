# A possible way of creating the needed MySQL table.
user, pwd, db = 'ine_student', 'ine-password', 'ine'
host, port = 'localhost', '3306'
con_dest = mysql.connector.connect(database=db, host=host, user=user, password=pwd, port=port)
cur_dest = con_dest.cursor()

# create MySQL table
sql_create_tweets = '''
CREATE TABLE IF NOT EXISTS Tweets (
    tweet_id DECIMAL(18) PRIMARY KEY,
    airline_sentiment TEXT,
    airline_sentiment_confidence REAL,
    negativereason TEXT,
    negativereason_confidence REAL,
    airline TEXT,
    airline_sentiment_gold TEXT,
    name TEXT,
    negativereason_gold TEXT,
    retweet_count INT,
    text TEXT,
    tweet_coord TEXT,
    tweet_created TIMESTAMP,
    tweet_location TEXT,
    user_timezone TEXT
    );
'''
cur_dest.execute("DROP TABLE IF EXISTS Tweets;")
cur_dest.execute(sql_create_tweets)
con_dest.commit()

con_src = sqlite3.connect('Airline-Tweets.sqlite') 
cur_src = con_src.cursor()
cur_src.execute("SELECT * FROM Tweets")

# Offset indicated in SQLite
cur_dest.execute("SET time_zone = '-08:00';")

sql_insert = """
INSERT INTO Tweets 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""
for src_row in cur_src:
    row = [data or None for data in src_row]
    timestamp = row[12][:19]  # Omit offset portion
    row[12] = timestamp
    row = tuple(row)
    cur_dest.execute(sql_insert, row)
    
con_dest.commit()

from pprint import pprint
cur_dest.execute("SELECT * FROM Tweets LIMIT 2;")
cols = [c[0] for c in cur_dest.description]
for row in cur_dest:
    pprint(dict(zip(cols, row)))