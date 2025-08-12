import os
import pandas as pd
import pdfkit
wkhtmltopdf_path = os.getenv('WKHTMLTOPDF_PATH')
print(f"DEBUG: wkhtmltopdf_path={wkhtmltopdf_path!r}")

if wkhtmltopdf_path:
    config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)
    print("DEBUG: PDF configuration created with custom path")
else:
    config = None
    print("DEBUG: PDF configuration set to None, trying system default")


# 📁 Create reports directory
report_dir = "reports"
os.makedirs(report_dir, exist_ok=True)

# 📌 PDF export config using environment variable (if set)
wkhtmltopdf_path = os.getenv('WKHTMLTOPDF_PATH')  # Optional environment variable
if wkhtmltopdf_path:
    config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)
else:
    config = None  # Try default system path

def generate_simple_report(df, report_name):
    desc = df.describe(include='all').to_html()

    html_path = os.path.join(report_dir, f"{report_name}_simple_report.html")
    pdf_path = os.path.join(report_dir, f"{report_name}_simple_report.pdf")

    # Save HTML report
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(f"<h1>Simple Data Report - {report_name}</h1>")
        f.write(desc)

    print(f"✅ HTML report saved to: {html_path}")

    # Try to generate PDF report
    try:
        if config:
            pdfkit.from_file(html_path, pdf_path, configuration=config)
        else:
            pdfkit.from_file(html_path, pdf_path)
        print(f"📄 PDF report saved to: {pdf_path}")
    except Exception as e:
        print(f"⚠️ PDF generation failed: {e}")

def clean_data(df):
    import numpy as np
    import re

    df.columns = df.columns.str.strip()
    df = df.drop_duplicates()

    df = df[df['Name'].notnull() & (df['Name'].str.strip() != '')]

    df['Email'] = df['Email'].str.strip().str.lower()
    df['Email'] = df['Email'].apply(lambda x: x if pd.notnull(x) and re.match(r"[^@]+@[^@]+\.[^@]+", x) else np.nan)

    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
    median_age = df['Age'].median() 
    df['Age'] = df['Age'].fillna(median_age)
    df['Age'] = df['Age'].round().astype(int)

    country_map = {
        'usa': 'United States', 'USA': 'United States',
        'UK': 'United Kingdom', 'uk': 'United Kingdom'
    }
    df['Country'] = df['Country'].str.strip().replace(country_map)

    df['SignUpDate'] = pd.to_datetime(df['SignUpDate'], errors='coerce')

    df['Income'] = df['Income'].astype(str).str.replace(r'[^0-9\.-]', '', regex=True)
    df['Income'] = pd.to_numeric(df['Income'], errors='coerce')
    df = df[df['Income'].notnull() & (df['Income'] >= 0)]
    df['Income'] = df['Income'].round().astype(int)

    df['Status'] = df['Status'].str.strip().str.capitalize().fillna('Unknown')

    return df

if __name__ == "__main__":
    raw_data_path = "sample_data/messy_data.csv"
    cleaned_data_path = "outputs/cleaned_data.csv"

    print("📥 Loading raw data...")
    raw_df = pd.read_csv(raw_data_path)

    print("📊 Generating simple raw data report...")
    generate_simple_report(raw_df, "raw_data")

    print("🧼 Cleaning data...")
    cleaned_df = clean_data(raw_df)

    print("💾 Saving cleaned data...")
    os.makedirs(os.path.dirname(cleaned_data_path), exist_ok=True)
    cleaned_df.to_csv(cleaned_data_path, index=False)

    print("📊 Generating simple cleaned data report...")
    generate_simple_report(cleaned_df, "cleaned_data")

    print("✅ Pipeline complete. Check the reports and cleaned data.")
