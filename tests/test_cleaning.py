import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
import numpy as np
# test_cleaning.py
from scripts.full_cleaning_pipeline import clean_data

def test_email_validation():
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob'],
        'Email': ['alice@example.com', 'invalid-email'],
        'Age': [25, 30],
        'Country': ['usa', 'UK'],
        'SignUpDate': ['2023-01-01', '2023-02-01'],
        'Income': ['50000', '60000'],
        'Status': ['active', 'inactive']
    })
    cleaned = clean_data(df)
    assert cleaned['Email'].iloc[0] == 'alice@example.com'
    assert pd.isna(cleaned['Email'].iloc[1])

def test_country_standardization():
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob'],
        'Email': ['a@b.com', 'b@c.com'],
        'Age': [25, 30],
        'Country': ['usa', 'UK'],
        'SignUpDate': ['2023-01-01', '2023-02-01'],
        'Income': ['50000', '60000'],
        'Status': ['active', 'inactive']
    })
    cleaned = clean_data(df)
    assert cleaned['Country'].iloc[0] == 'United States'
    assert cleaned['Country'].iloc[1] == 'United Kingdom'

def test_age_imputation():
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Email': ['a@b.com', 'b@c.com', 'c@d.com'],
        'Age': [25, np.nan, 35],
        'Country': ['usa', 'UK', 'usa'],
        'SignUpDate': ['2023-01-01', '2023-02-01', '2023-03-01'],
        'Income': ['50000', '60000', '70000'],
        'Status': ['active', 'inactive', 'active']
    })
    cleaned = clean_data(df)
    median_age = cleaned['Age'].median()
    # Check that the missing age value was filled with the median
    assert cleaned['Age'].iloc[1] == median_age
