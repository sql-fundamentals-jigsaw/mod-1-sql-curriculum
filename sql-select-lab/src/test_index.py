from index import *


def test_all_employees_returns_twelve_entries():
    assert len(all_employees()) == 12

def test_all_employees_has_each_entry_an_employee():
    assert all_employees()[0] == (1, 'Tom', 'manager',
            '2019-05-20', 10001, '212-438-3984')

def test_all_ingredients_selects_ingredients():
    assert len(all_ingredients()) == 20

    

def test_all_ingredient_names_returns_twenty_entries():
    assert len(all_ingredient_names()) == 20

def test_all_employee_names_returns_only_the_name():
    assert (all_ingredient_names()[0]) == ('baby spinach',)


def test_all_employee_start_dates_returns_only_start_dates():
    assert all_employee_start_dates()[0] == ('2019-05-20',)

def test_all_employee_start_dates_returns_twelve_entries():
    assert len(all_employee_start_dates()) == 12
    

def test_all_cheaper_ingredients():
    assert all([ingredient[2] < 1 for ingredient in cheaper_ingredients()])


def test_naomi_start_date():
    assert naomi_start_date() == [('2019-02-12',)]


def test_ingredients_middle_price():
    assert all([(ingredient[2] < 1.50 or ingredient[2] > 1) for ingredient in ingredients_middle_price()])


def test_employees_nearby_zip_code():
    assert all([(employee[-2] == 10001 or employee[-2] == 10002) for employee in employees_in_nearby_zip_code()])
