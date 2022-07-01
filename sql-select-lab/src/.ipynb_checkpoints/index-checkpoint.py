
import sqlite3
import pandas as pd
conn = sqlite3.connect('../grocery.db')
cursor = conn.cursor()

def load_data_to_sql():
    employees_url = "https://raw.githubusercontent.com/jigsawlabs-student/mod-1-sql-curriculum/master/1-sql-fundamentals/8-sql-select-lab/data/employees.csv"
    ingredients_url = "https://raw.githubusercontent.com/jigsawlabs-student/mod-1-sql-curriculum/master/1-sql-fundamentals/8-sql-select-lab/data/ingredients.csv"
    ingredients_df = pd.read_csv(ingredients_url)
    employees_df = pd.read_csv(employees_url)
    ingredients_df.to_sql('ingredients', conn,
                      index = False, if_exists = 'replace')
    employees_df.to_sql('employees', conn, index = False,
            if_exists = 'replace')


def all_employees():
    cursor.execute('SELECT * FROM employees;')
    return cursor.fetchall()

def all_ingredients():
    cursor.execute('SELECT * FROM ingredients;')
    return cursor.fetchall()

def all_ingredient_names():
    cursor.execute('SELECT name FROM ingredients;')
    return cursor.fetchall()

def all_employee_start_dates():
    cursor.execute('SELECT start_date FROM employees;')
    return cursor.fetchall()

def cheaper_ingredients():
    cursor.execute("SELECT * FROM ingredients WHERE cost_per_ounce < 1.0")
    return cursor.fetchall()

def naomi_start_date():
    cursor.execute("SELECT start_date FROM employees WHERE name = 'Naomi'")
    return cursor.fetchall()

def ingredients_expiring_after_feb():
    cursor.execute("SELECT * FROM ingredients WHERE expiration >= '2020-02-01'")
    return cursor.fetchall()

def ingredients_middle_price():
    cursor.execute("SELECT * FROM ingredients WHERE cost_per_ounce > 1 AND cost_per_ounce < 1.50")
    return cursor.fetchall()

def employees_in_nearby_zip_code():
    cursor.execute("SELECT * FROM employees WHERE zip_code = 10001 or zip_code = 10002")
    return cursor.fetchall()
