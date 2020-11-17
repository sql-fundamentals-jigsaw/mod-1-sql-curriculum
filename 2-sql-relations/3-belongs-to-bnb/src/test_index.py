from index import *
def test_listing_name_of_highest_price():
    assert listing_name_of_highest_price() == [('Furnished room in Astoria apartment',)]

def test_id_of_location_with_lowest_longitude():
    assert id_of_location_with_lowest_longitude() == [(45652,)]

def test_greatest_occupancy_of_listing():
    assert greatest_occupancy_of_listing() == [(365,)]

def test_avg_price_of_listing():
    assert avg_price_of_listing() == [(152.7206871868289,)]

def test_number_of_hosts():
    assert number_of_hosts() == [(37457,)]

def test_longitude_and_latitude_of_listing_with_highest_price():
    assert longitude_and_latitude_of_listing_with_highest_price() ==  [(-73.92, 40.77)]

def test_neighborhood_id_of_lowest_price_listing():
    assert neighborhood_id_of_lowest_price_listing() == [(6,)]

def test_long_lat_of_lowest_price_listing():
    assert long_lat_of_lowest_price_listing() == [(-73.95, 40.69)]  
    
def test_host_with_most_reviews():
    assert host_with_most_reviews() == [('Maya', 2273)]


def test_host_name_with_lowest_avg_listing_price():
    assert host_name_with_lowest_avg_listing_price() == [('Aymeric',)]

def test_neighborhood_with_most_locations():
    assert neighborhood_with_most_locations() == [('Williamsburg',)]

def test_neighborhood_with_exactly_ten_locations():
    assert neighborhood_with_exactly_ten_locations() == [('North Riverdale',), ('Great Kills',),
 ('East Morrisania',), ('Melrose',), ('Bergen Beach',), ('Westchester Square',)]


    
    

    
    

    
    
