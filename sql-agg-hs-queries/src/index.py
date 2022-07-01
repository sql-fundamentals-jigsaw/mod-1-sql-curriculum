import sqlite3
import pandas as pd
conn = sqlite3.connect('high_schools.db')
cursor = conn.cursor()

def load_data():
    url = "https://raw.githubusercontent.com/data-eng-10-21/sql-agg-hs-queries/master/highschools.csv"
    high_school_df = pd.read_csv(url)
    high_school_df.to_sql('high_schools', conn, 
            index = False, if_exists = 'replace')

def all_high_schools():
    pass

def avg_num_students_in_hs():
    pass

def avg_attendance_rate_in_hs():
    pass

def largest_diff_btwn_grad_rate_and_college_career_rate():
    pass

def highest_math_avg_queens():
    pass

def highest_combined_score():
    pass

def avg_num_of_students_per_borough():
    pass
    
def avg_diff_btwn_grad_rate_and_college_career_rate_by_boro():
    pass


def boroughs_with_avg_total_students_over_one_thousand():
    pass

def boroughs_with_avg_college_career_under_point_six():
    pass
