import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'code'))) # had to add this line to get the import to work
print(f"Current sys.path: {sys.path}")  # Check if 'code' folder is in sys.path

from code.etl import top_locations, top_locations_mappable, tickets_in_top_locations

import pandas as pd



def test_should_pass():
    print("\nAlways True!")
    assert True

def test_top_locations():
    # Arrange the test variables
    violations_df = pd.read_csv('./cache/final_cuse_parking_violations.csv')
    expect_row_count = 135
    expect_col_count = 2
    expect_col_names = ['amount', 'location']

    # act on the function under test
    top_locations_df = top_locations(violations_df)

    # assert what is expected actually happened
    print(f"\nTesting row count of {expect_row_count}...")
    assert len(top_locations_df) == expect_row_count
    
    print(f"\nTesting column count of {expect_col_count}...")
    assert len(top_locations_df.columns) == expect_col_count

    print(f"\nTesting column names are  {expect_col_names}...")
    assert set(top_locations_df.columns) == set(expect_col_names)

def test_top_locations_mappable():
    # Arrange the test variables
    violations_df = pd.read_csv('./cache/final_cuse_parking_violations.csv')
    expect_row_count = 135
    expect_col_count = 4
    expect_col_names = ['amount', 'lat', 'location','lon'] # order does not matter

    # act on the function under test
    top_locations_df = top_locations_mappable(violations_df)

    # assert what is expected actually happened
    print(f"\nTesting row count of {expect_row_count}...")
    assert len(top_locations_df) == expect_row_count
    
    print(f"\nTesting column count of {expect_col_count}...")
    assert len(top_locations_df.columns) == expect_col_count

    print(f"\nTesting column names are  {expect_col_names}...")
    assert set(top_locations_df.columns) == set(expect_col_names)

def test_tickets_in_top_locations():
        # Arrange the test variables
    violations_df = pd.read_csv('./cache/final_cuse_parking_violations.csv')
    expect_row_count = 8109
    expect_col_count = 11
    expect_col_names = ['location','ticket_number','issued_date',
                        'description','status','dayofweek',
                        'hourofday','lat','lon','count','amount'] # order does not matter

    # act on the function under test
    top_locations_df =tickets_in_top_locations(violations_df)

    # assert what is expected actually happened
    print(f"\nTesting row count of {expect_row_count}...")
    assert len(top_locations_df) == expect_row_count
    
    print(f"\nTesting column count of {expect_col_count}...")
    assert len(top_locations_df.columns) == expect_col_count

    print(f"\nTesting column names are  {expect_col_names}...")
    assert set(top_locations_df.columns) == set(expect_col_names)