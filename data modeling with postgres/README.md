Project: Data Modeling using Postgre database Introduction A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to.

Project Description For this project, I modeled data using Postgres database and built an ETL pipeline using Python for data extraction transofmration and loading. The ETL pipeline transfers data from files located in two local directories into the Postgres database using Python and SQL Using a Star model, I have created 1 fact and 4 dimension tables

The Star Schema is used since its is a special, simplified case of the snowflake schema.

Schema for Song Play Analysis

Fact Table songplays - records in log data associated with song plays i.e. records with page NextSong songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

Dimension Tables users - users in the app user_id, first_name, last_name, gender, level songs - songs in music database song_id, title, artist_id, year, duration artists - artists in music database artist_id, name, location, latitude, longitude time - timestamps of records in songplays broken down into specific units start_time, hour, day, week, month, year, weekday

All tables created have relevant comments / docstring.

Files in repository test.ipnb displays the first few rows of each table to let you check your database create_tables.py drops and created your table etl.ipynb read and processes a single file from song_data and log_data and loads into the tables etl.py reads and processes files from song_data and log_data and loads them into your tables. sql_queries.py containg all your sql queries and in imported into the last three files above

When all the task was completed, the I ran the python file in the terminal starting from the (1)sql_queries.py (2) create_tables.py and then (3)etl.py. I then run the test.ipnb to check that all my test passed. I used what I completed in etl.ipynb to complete etl.py.