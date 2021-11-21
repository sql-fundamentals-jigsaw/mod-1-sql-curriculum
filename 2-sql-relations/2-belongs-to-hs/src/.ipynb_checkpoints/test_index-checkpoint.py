from index import *

def test_borough_of_school_with_highest_writing_score():
    assert borough_of_school_with_highest_writing_score() ==[('M', 682.0)]

def test_borough_of_school_with_lowest_math_avg():
    assert borough_of_school_with_lowest_math_avg() == [('X', 312.0)]

def test_highest_math_avg_schools_over_one_thousand_students():
    assert highest_math_avg_schools_over_one_thousand_students() == [(735.0,)]

def test_avg_num_test_takers_per_borough():
    assert avg_num_test_takers_per_borough() == [('K', 126.33673469387755),
 ('M', 110.34177215189874),
 ('Q', 199.51666666666668),
 ('R', 300.5),
 ('X', 80.3875)]

def test_avg_grad_rate_of_schools_with_math_avg_over_five_hundred():
    assert avg_grad_rate_of_schools_with_math_avg_over_five_hundred() == [(0.9769999999999999,)]

def test_total_test_takers_per_borough():
    assert total_test_takers_per_borough() == [('K', 12381.0), ('M', 8717.0), ('Q', 11971.0), ('R', 3005.0), ('X', 6431.0)]

def test_avg_combined_reading_and_math_per_borough():
    assert avg_combined_reading_and_math_per_borough() == [('K', 795.2857142857143),
 ('M', 869.5822784810126),
 ('Q', 874.5666666666667),
 ('R', 930.0),
 ('X', 778.2375)]

def test_schools_with_largest_diff_btwn_num_test_takers_and_students():
    assert schools_with_largest_diff_btwn_num_test_takers_and_students() == [('Brooklyn Technical High School', 4561.0),
 ('Fort Hamilton High School', 3888.0),
 ('Francis Lewis High School', 3623.0),
 ('Midwood High School', 3234.0),
 ('James Madison High School', 3139.0)]

def test_difference_btwn_total_students_and_test_takers_per_borough():
    assert difference_btwn_total_students_and_test_takers_per_borough()  == [('R', 15627.0),
 ('X', 35972.0),
 ('M', 41118.0),
 ('Q', 58712.0),
 ('K', 61192.0)]


