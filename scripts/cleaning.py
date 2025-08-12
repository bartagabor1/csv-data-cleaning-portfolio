import pandas as pd
import numpy as np
import re

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans a raw DataFrame by:
    - Stripping whitespace
    - Dropping duplicates
    - Validating emails
    - Imputing missing age values with the median
    - Standardizing country names
    - Parsing dates
    - Cleaning income values
    - Capitalizing status
    """

    # Strip column names
    df.columns = df.columns.str.strip()

    # Drop duplicates
    df = df.drop_duplicates()

    # Drop rows with missing or blank Name
    df = df[df['Name'].notnull() & (df['Name'].str.strip() != '')]

    # Clean and validate Email
    df['Email'] = df['Email'].str.strip().str.lower()
    df['Email'] = df['Email'].apply(
        lambda x: x if pd.notnull(x) and re.match(r"[^@]+@[^@]+\.[^@]+", x) else np.nan
    )

    # Clean Age (convert to numeric, fill missing with median)
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
    median_age = df['Age'].median()
    df['Age'] = df['Age'].fillna(median_age)
    df['Age'] = df['Age'].round().astype(int)

    # Standardize Country names
    country_map = {
        'usa': 'United States', 'USA': 'United States',
        'uk': 'United Kingdom', 'UK': 'United Kingdom'
    }
    df['Country'] = df['Country'].str.strip().replace(country_map)

    # Convert SignUpDate to datetime
    df['SignUpDate'] = pd.to_datetime(df['SignUpDate'], errors='coerce')

    # Clean and validate Income
    df['Income'] = df['Income'].astype(str).str.replace(r'[^0-9\.-]', '', regex=True)
    df['Income'] = pd.to_numeric(df['Income'], errors='coerce')
    df = df[df['Income'].notnull() & (df['Income'] >= 0)]
    df['Income'] = df['Income'].round().astype(int)

    # Capitalize and fill Status
    df['Status'] = df['Status'].str.strip().str.capitalize().fillna('Unknown')

    return df
