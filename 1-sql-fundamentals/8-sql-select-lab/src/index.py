
import sqlite3
import pandas as pd
conn = sqlite3.connect('grocery.db')
cursor = conn.cursor()

def load_data_to_sql():
    employees_url = "https://raw.githubusercontent.com/jigsawlabs-student/mod-1-sql-curriculum/master/1-sql-fundamentals/8-sql-select-lab/employees.csv"
    ingredients_url = "https://raw.githubusercontent.com/jigsawlabs-student/mod-1-sql-curriculum/master/1-sql-fundamentals/8-sql-select-lab/ingredients.csv"
    ingredients_df = pd.read_csv(ingredients_url)
    employees_df = pd.read_csv(employees_url)

def all_employees():
    cursor.execute('SELECT * FROM employees;')
    return cursor.fetchall()

def all_ingredients():
    cursor.execute('SELECT * FROM ingredients;')
    return cursor.fetchall()

