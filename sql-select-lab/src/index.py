
import sqlite3
import pandas as pd
conn = sqlite3.connect('../grocery.db')
cursor = conn.cursor()

def load_data_to_sql():
    employees_url = "https://raw.githubusercontent.com/data-eng-10-21/mod-1-sql-curriculum/master/1-sql-fundamentals/8-sql-select-lab/data/employees.csv"
    ingredients_url = "https://raw.githubusercontent.com/data-eng-10-21/mod-1-sql-curriculum/master/1-sql-fundamentals/8-sql-select-lab/data/ingredients.csv"
    ingredients_df = pd.read_csv(ingredients_url)
    employees_df = pd.read_csv(employees_url)
    ingredients_df.to_sql('ingredients', conn,
                      index = False, if_exists = 'replace')
    employees_df.to_sql('employees', conn, index = False,
            if_exists = 'replace')


def all_employees():
    pass

def all_ingredients():
    pass

def all_ingredient_names():
    pass

def all_employee_start_dates():
    pass

def cheaper_ingredients():
    pass

def naomi_start_date():
    pass

def ingredients_expiring_after_feb():
    pass

def ingredients_middle_price():
    pass

def employees_in_nearby_zip_code():
    pass
    # in zip codes 10001 or 10002
