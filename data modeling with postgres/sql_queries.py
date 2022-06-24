# DROP TABLES

songplay_table_drop = "Drop TABLE IF EXISTS songplays"
user_table_drop = "Drop TABLE IF EXISTS users"
song_table_drop = "Drop TABLE IF EXISTS songs"
artist_table_drop = "Drop TABLE IF EXISTS artists"
time_table_drop = "Drop TABLE IF EXISTS time"

# CREATE TABLES

# fact table - data about song
# songplay_table_create = ("""
# CREATE TABLE IF NOT EXISTS songplays (
#     songplay_id int PRIMARY KEY ,
#     start_time timestamp with time zone NOT NULL,
#     user_id INTEGER NOT NULL,
#     level VARCHAR(15),
#     song_id VARCHAR(25),
#     artist_id VARCHAR(25),
#     session_id INTEGER,
#     location VARCHAR(50),
#     user_agent VARCHAR(150)
# );
# """)

# fact table - data about song
songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id int PRIMARY KEY ,
    start_time timestamp NOT NULL,
    user_id INTEGER NOT NULL REFERENCES users (user_id),
    level VARCHAR(15) not null,
    song_id VARCHAR(25) REFERENCES songs (song_id),
    artist_id VARCHAR(25) REFERENCES artists (artist_id),
    session_id INTEGER not null,
    location VARCHAR(50),
    user_agent VARCHAR(150)
);
""")


#dimension table - user
user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    first_name VARCHAR(50) not null,
    last_name VARCHAR(50) not null,
    gender CHAR(1),
    level VARCHAR(15) not null
);
""")

#dimension table - songs
song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
    song_id VARCHAR(25) PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    artist_id VARCHAR(25) NOT NULL REFERENCES artists(artist_id),
    year INTEGER NOT NULL,
    duration FLOAT NOT NULL
);
""")

#dimension table - artist
artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
    artist_id VARCHAR(25) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(100),
    latitude double precision,
    longitude  double precision
);
""")

#dimension table - time
# time_table_create = ("""
# CREATE TABLE IF NOT EXISTS time (
#     start_time TIMESTAMP with time zone PRIMARY KEY,
#     hour INTEGER not null,
#     day INTEGER not null,
#     week INTEGER not null,
#     month INTEGER not null,
#     year INTEGER not null,
#     weekday INTEGER not null
# );
# """)

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
        start_time TIMESTAMP PRIMARY KEY,
        hour NUMERIC NOT NULL,
        day NUMERIC NOT NULL,
        week NUMERIC NOT NULL,
        month NUMERIC NOT NULL,
        year NUMERIC NOT NULL,
        weekday NUMERIC NOT NULL
    )
""")


# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT(songplay_id) DO NOTHING;

-- alter table songplays alter column song_id set not null; 
-- alter table songplays alter column artist_id set not null; 

""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level;
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude)
VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;
""")

# FIND SONGS

song_select = ("""
SELECT songs.song_id, songs.artist_id FROM songs 
JOIN artists on songs.artist_id = artists.artist_id
WHERE songs.title = %s
AND artists.name = %s
AND songs.duration = %s
;
""")

# QUERY LISTS

create_table_queries = [time_table_create, user_table_create, artist_table_create, song_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
