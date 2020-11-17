import sqlite3
import pandas as pd
conn = sqlite3.connect('schools.db')
cursor = conn.cursor()

highschools_url = "https://raw.githubusercontent.com/jigsawlabs-student/mod-1-sql-curriculum/master/2-sql-relations/2-belongs-to-hs/highschools.csv"
sat_records_url = "https://raw.githubusercontent.com/jigsawlabs-student/mod-1-sql-curriculum/master/2-sql-relations/2-belongs-to-hs/sat_records.csv"
df_hs = pd.read_csv(highschools_url)
df_sat = pd.read_csv(sat_records_url)
df_hs.to_sql('high_schools' ,conn, index = False, if_exists = 'replace')
df_sat.to_sql('sat_records' ,conn, index = False, if_exists = 'replace')

def all_tables():
    cursor.execute('SELECT name from sqlite_master where type= "table"')
    return cursor.fetchall()

def high_school_schema():
    cursor.execute('PRAGMA table_info(high_schools)')
    cursor.fetchall()

def sat_records_schema():
    cursor.execute('PRAGMA table_info(sat_records)')
    cursor.fetchall()

def borough_of_school_with_highest_writing_score():
    cursor.execute("""SELECT schools.boro,
       MAX(sat.writing_score) FROM sat_records AS sat
       JOIN high_schools AS schools ON sat.dbn = schools.dbn;""")
    return cursor.fetchall()

def borough_of_school_with_lowest_math_avg():
    cursor.execute("""SELECT schools.boro,
       MIN(sat.math_avg) FROM sat_records AS sat
       JOIN high_schools AS schools ON sat.dbn = schools.dbn; """)
    return cursor.fetchall()

def highest_math_avg_schools_over_one_thousand_students():
    cursor.execute("""SELECT MAX(sat.math_avg)
  FROM sat_records AS sat JOIN
       high_schools AS schools ON sat.dbn = schools.dbn
 WHERE schools.total_students > 1000; """)
    return cursor.fetchall()

def avg_num_test_takers_per_borough():
    cursor.execute(""" SELECT schools.boro,
       AVG(sat.num_test_takers) FROM sat_records AS sat
       JOIN
       high_schools AS schools ON sat.dbn = schools.dbn
 GROUP BY schools.boro;""")
    return cursor.fetchall()

def avg_grad_rate_of_schools_with_math_avg_over_five_hundred():
    cursor.execute("""SELECT AVG(schools.graduation_rate)
  FROM sat_records AS sat JOIN high_schools AS schools 
  ON sat.dbn = schools.dbn WHERE sat.math_avg > 500; """)
    return cursor.fetchall()

def total_test_takers_per_borough():
    cursor.execute("""SELECT schools.boro, SUM(sat.num_test_takers)
  FROM sat_records AS sat JOIN high_schools AS schools ON sat.dbn = schools.dbn
 GROUP BY schools.boro;
 """)
    return cursor.fetchall()

def avg_combined_reading_and_math_per_borough():
    cursor.execute("""SELECT schools.boro, AVG(sat.math_avg + sat.reading_avg)
  FROM sat_records AS sat JOIN high_schools AS schools ON sat.dbn = schools.dbn
 GROUP BY schools.boro;""")
    return cursor.fetchall()

def schools_with_largest_diff_btwn_num_test_takers_and_students():
    cursor.execute("""
SELECT schools.school_name,
       (schools.total_students - sat.num_test_takers) AS difference
  FROM sat_records AS sat
       JOIN
       high_schools AS schools ON sat.dbn = schools.dbn
 ORDER BY difference DESC
 LIMIT 5;
 """)
    return cursor.fetchall()

def difference_btwn_total_students_and_test_takers_per_borough():
    cursor.execute("""
SELECT schools.boro,
       SUM(schools.total_students - sat.num_test_takers) AS difference
  FROM sat_records AS sat
       JOIN
       high_schools AS schools ON sat.dbn = schools.dbn
 GROUP BY schools.boro
 ORDER BY difference;

 """)
    return cursor.fetchall()
