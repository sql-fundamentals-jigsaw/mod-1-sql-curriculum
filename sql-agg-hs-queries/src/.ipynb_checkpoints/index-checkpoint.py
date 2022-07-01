import sqlite3
import pandas as pd
conn = sqlite3.connect('high_schools.db')
cursor = conn.cursor()

def load_data():
    url = "https://raw.githubusercontent.com/jigsawlabs-student/sql-agg-hs-queries/master/highschools.csv"
    high_school_df = pd.read_csv(url)
    high_school_df.to_sql('high_schools', conn, 
            index = False, if_exists = 'replace')

def all_high_schools():
    return cursor.execute('SELECT * from high_schools;')

def avg_num_students_in_hs():
    cursor.execute("""SELECT AVG(total_students) FROM high_schools WHERE boro = "M";""")
    return cursor.fetchall()

def avg_attendance_rate_in_hs():
    cursor.execute("""SELECT AVG(attendance_rate) FROM 
    high_schools WHERE boro = "M";""")
    return cursor.fetchall()

def largest_diff_btwn_grad_rate_and_college_career_rate():
    cursor.execute("""SELECT MAX(graduation_rate - college_career_rate) 
    FROM high_schools;""")
    return cursor.fetchall()

def highest_math_avg_queens():
    cursor.execute("""SELECT MAX(math_avg) FROM 
    high_schools WHERE boro = "Q";""")
    return cursor.fetchall()

def highest_combined_score():
    cursor.execute("""SELECT MAX(math_avg + reading_avg) FROM 
    high_schools WHERE boro = "M";""")
    return cursor.fetchall()

def avg_num_of_students_per_borough():
    cursor.execute("""SELECT boro, AVG(total_students) 
    FROM high_schools GROUP BY boro;""")
    return cursor.fetchall()
    
def avg_diff_btwn_grad_rate_and_college_career_rate_by_boro():
    cursor.execute("""SELECT boro, AVG(graduation_rate - college_career_rate) FROM high_schools GROUP BY boro;""")
    return cursor.fetchall()


def boroughs_with_avg_total_students_over_one_thousand():
    cursor.execute("""SELECT boro, AVG(total_students) FROM high_schools
 GROUP BY boro HAVING AVG(total_students) > 1000;""")
    return cursor.fetchall()

def boroughs_with_avg_college_career_under_point_six():
    cursor.execute("""SELECT boro, AVG(college_career_rate) 
    FROM high_schools GROUP BY boro HAVING AVG(college_career_rate) < 0.6;""")
    return cursor.fetchall()
