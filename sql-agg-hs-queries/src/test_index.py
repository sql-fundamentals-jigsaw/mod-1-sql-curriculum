from index import *
def all_high_schools():
    return cursor.execute('select * from high_schools;')

def test_avg_num_students_in_hs():
    assert avg_num_students_in_hs() == [(601.9666666666667,)]

def test_avg_attendance_rate_in_hs():
    assert avg_attendance_rate_in_hs() == [(0.8782222222222222,)]

def test_largest_diff_btwn_grad_rate_and_college_career_rate():
    assert largest_diff_btwn_grad_rate_and_college_career_rate() == [(0.55,)]

def test_highest_math_avg_queens():
    assert highest_math_avg_queens() ==  [(660.0,)]

def test_highest_combined_score():
    assert highest_combined_score() == [(1414.0,)]


def test_avg_num_of_students_per_borough():
    assert avg_num_of_students_per_borough() == [('K', 740.2884615384615), 
            ('M', 601.9666666666667),
            ('Q', 1135.4615384615386),
            ('R', 1863.2),
            ('X', 523.4827586206897)]
    
def test_avg_diff_btwn_grad_rate_and_college_career_rate_by_boro():
    assert avg_diff_btwn_grad_rate_and_college_career_rate_by_boro() == [('K', 0.22480392156862752),
            ('M', 0.17298850574712643),
            ('Q', 0.1706153846153846),
            ('R', 0.23200000000000004),
            ('X', 0.21264367816091953)]


def test_boroughs_with_avg_total_students_over_one_thousand():
    assert boroughs_with_avg_total_students_over_one_thousand() == [('Q', 1135.4615384615386), ('R', 1863.2)]

def test_boroughs_with_avg_college_career_under_point_six():
    assert boroughs_with_avg_college_career_under_point_six() == [('K', 0.5471568627450981), ('X', 0.5295402298850576)]
