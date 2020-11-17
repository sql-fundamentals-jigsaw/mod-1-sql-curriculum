import sqlite3
conn = sqlite3.connect('airbnb.db')
cursor = conn.cursor()

import pandas as pd
neighborhoods_url = "https://raw.githubusercontent.com/jigsawlabs-student/mod-1-sql-curriculum/master/2-sql-relations/3-belongs-to-bnb/neighborhoods.csv"
hosts_url = "https://raw.githubusercontent.com/jigsawlabs-student/mod-1-sql-curriculum/master/2-sql-relations/3-belongs-to-bnb/hosts.csv"
locations_url = "https://raw.githubusercontent.com/jigsawlabs-student/mod-1-sql-curriculum/master/2-sql-relations/3-belongs-to-bnb/locations.csv"
listings_url = "https://raw.githubusercontent.com/jigsawlabs-student/mod-1-sql-curriculum/master/2-sql-relations/3-belongs-to-bnb/listings.csv"

hosts_df = pd.read_csv(hosts_url)
neighborhoods_df = pd.read_csv(neighborhoods_url)

locations_df = pd.read_csv(locations_url)
listings_df = pd.read_csv(listings_url)

hosts_df.to_sql('hosts',conn, index = False, if_exists = 'replace')
neighborhoods_df.to_sql('neighborhoods',conn, index = False, if_exists = 'replace')
locations_df.to_sql('locations',conn, index = False, if_exists = 'replace')
listings_df.to_sql('listings', conn, index = False, if_exists = 'replace')


def display_tables():
    cursor.execute('SELECT name from sqlite_master where type= "table"')
    return cursor.fetchall()

def display_schema(table_name):
    cursor.execute(f"PRAGMA table_info({table_name})")
    cursor.fetchall()

def listing_name_of_highest_price():
    cursor.execute('SELECT name FROM listings ORDER BY price DESC LIMIT 1;')
    return cursor.fetchall()

def id_of_location_with_lowest_longitude():
    cursor.execute('SELECT id FROM locations ORDER BY longitude LIMIT 1;')
    return cursor.fetchall()

def greatest_occupancy_of_listing():
    cursor.execute('SELECT MAX(occupancy) FROM listings;')
    return cursor.fetchall()

def avg_price_of_listing():
    cursor.execute('SELECT AVG(price) FROM listings;')
    return cursor.fetchall()

def number_of_hosts():
    cursor.execute('SELECT COUNT(id) FROM hosts;')
    return cursor.fetchall()

def longitude_and_latitude_of_listing_with_highest_price():
    cursor.execute(""" SELECT ROUND(a.longitude, 2), ROUND(a.latitude, 2)
       FROM locations AS a JOIN
       listings AS b ON a.id = b.location_id ORDER BY b.price DESC
 LIMIT 1; """)
    return cursor.fetchall()

def neighborhood_id_of_lowest_price_listing():
    cursor.execute(""" SELECT a.neighborhood_id
       FROM locations AS a
       JOIN listings AS b ON a.id = b.location_id
 ORDER BY b.price LIMIT 1;
""")
    return cursor.fetchall()

def long_lat_of_lowest_price_listing():
    cursor.execute("""SELECT ROUND(a.longitude, 2),
       ROUND(a.latitude, 2) FROM locations AS a
       JOIN listings AS b ON a.id = b.location_id
 ORDER BY b.price LIMIT 1;""")
    return cursor.fetchall()

def host_with_most_reviews():
    cursor.execute(""" SELECT h.host_name,
       SUM(l.number_of_reviews) FROM hosts AS h
       JOIN listings AS l ON h.id = l.host_id
 GROUP BY l.host_id ORDER BY SUM(l.number_of_reviews) DESC
 LIMIT 1;""")
    return cursor.fetchall()


def host_name_with_lowest_avg_listing_price():
    cursor.execute("""SELECT h.host_name FROM hosts AS h
       JOIN
       listings AS l ON h.id = l.host_id GROUP BY l.host_id
 ORDER BY AVG(l.price) LIMIT 1; """)
    return cursor.fetchall()

def neighborhood_with_most_locations():
    cursor.execute("""SELECT n.name FROM neighborhoods AS n
       JOIN
       locations AS l ON n.id = l.neighborhood_id
 GROUP BY n.id ORDER BY COUNT(n.id) DESC LIMIT 1;""")
    return cursor.fetchall()

def neighborhood_with_exactly_ten_locations():
    cursor.execute("""SELECT n.name
  FROM neighborhoods AS n JOIN
       locations AS l ON n.id = l.neighborhood_id
 GROUP BY n.id HAVING COUNT(n.id) = 10; """)
    return cursor.fetchall()
    

    
    

    
    

    
    
