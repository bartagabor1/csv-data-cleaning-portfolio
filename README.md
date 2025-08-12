# 🧼 	CSV Data Cleaning Portfolio – Clean Customer Dataset

Welcome! This project demonstrates professional-level data cleaning using Python and Pandas on a realistic, messy customer dataset.

---

## 📌 Project Overview

- **Goal:** Clean and preprocess a synthetic customer dataset with typical real-world issues such as missing values, inconsistent formatting, and invalid entries.
- **Tech:** Python, Pandas, NumPy, Regex, Jupyter Notebook, PDF/HTML reporting
- **Outputs:** 
  - Cleaned CSV file  
  - Auto-generated reports in **HTML** and **PDF** formats  
  - Unit tests for cleaning logic
  - Optional pipeline abstraction
---

## 🗂️ Directory Structure

```
├── sample_data/
│ └── messy_data.csv                   # Raw synthetic input file
├── outputs/
│ └── cleaned_data.csv                 # Final cleaned output
├── reports/
│ ├── raw_data_simple_report.html      # Raw data HTML report
│ ├── raw_data_simple_report.pdf       # Raw data PDF report
│ ├── cleaned_data_simple_report.html  # Cleaned data HTML report
│ ├── cleaned_data_simple_report.pdf   # Cleaned data PDF report
│ └── data_cleaning_summary.html       # Clickable HTML summary report
├── scripts/
│ ├── cleaning.py                      # Python script for data cleaning
│ └── full_cleaning_pipeline.py        # # Main script (reporting + cleaning)
├── pipeline.py                        # Optional: Class-based OOP pipeline 
├── tests/
│ ├── test_cleaning.py                 # Unit tests for cleaning functions
│ └── testing.md                       # Optional: Testing guide (how/why)
├── notebooks/
│ └── eda.ipynb                        #  Exploratory Data Analysis notebook
├── cleaning_summary.md                # Summary of cleaning steps (Markdown)
├── wkhtmltopdf_setup.md               #  PDF report setup instructions
├── README.md                          # This file
└── requirements.txt                   # Python dependencies 
```

# Class-based OOP pipeline (DataCleaningPipeline)
## ⚙️ Data Cleaning Summary

The dataset was cleaned using custom logic in `clean_data.py`. Key transformations included:

| Step | Description |
|------|-------------|
| 🧹 Removed Duplicates | Dropped exact duplicate rows |
| 👤 Dropped Missing Names | Removed rows with null or empty `Name` values |
| 📧 Email Validation | Invalid emails replaced with `NaN` using regex |
| 🔢 Cleaned Age | Converted to numeric, filled nulls with median, rounded to int |
| 🌍 Country Standardization | Mapped variations like `"usa"` → `"United States"` |
| 📅 Sign-up Date Parsing | Converted to proper datetime format |
| 💰 Cleaned Income | Removed symbols, validated as numeric, dropped invalid |
| 📌 Status Normalization | Capitalized, trimmed, missing replaced with `'Unknown'`|

➡️ **View full summary in browser:**  
[📄 Open HTML Report](./reports/data_cleaning_summary.html)

Or check the Markdown version: [`cleaning_summary.md`](./cleaning_summary.md)

➡️ **See output reports:**  
- [Raw Report (HTML)](./reports/raw_data_simple_report.html)  
- [Cleaned Report (HTML)](./reports/cleaned_data_simple_report.html)

---

## 🧱 Class-based OOP Pipeline (Optional)

For advanced or reusable workflows, the entire pipeline is wrapped in a class inside `pipeline.py`. This allows you to run the full flow in just a few lines of code:

```bash
python
from pipeline import DataCleaningPipeline

pipeline = DataCleaningPipeline(
    raw_data_path="sample_data/messy_data.csv",
    cleaned_data_path="outputs/cleaned_data.csv",
    report_dir="reports"
)

pipeline.run()
```

The class handles reading, cleaning, saving, and report generation—ideal for production scenarios.

---

## 📊 EDA & Reporting

The optional [`notebooks/eda.ipynb`](./notebooks/eda.ipynb) notebook explores:

- Data types and nulls
- Distribution of age, income, and country
- Status breakdown
- Missing value visualization

---

## ✅ Unit Testing

We’ve included unit tests for the cleaning functions (e.g. email validation, country mapping, age imputation).

To run tests:
```bash
pytest
```

For full instructions, see: [`tests/testing.md`](./tests/testing.md)

---

## 🧾 PDF Setup (Optional)

To generate PDF reports using `pdfkit`, you’ll need to install **wkhtmltopdf** and configure the path.  
See detailed setup: [`wkhtmltopdf_setup.md`](./wkhtmltopdf_setup.md)

---

## 🧪 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/bartagabor1/csv-data-cleaning-portfolio.git
   cd csv-data-cleaning-portfolio
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the cleaning script:
   ```bash
   python scripts/full_cleaning_pipeline.py
   ```

4. Open the EDA notebook (optional):
   ```bash
   jupyter notebook notebooks/eda.ipynb
   ```

---

## 💻 Requirements

- Python 3.10+
- pandas  
- numpy  
- seaborn  
- matplotlib  
- missingno  
- pandas-profiling
- ydata-profiling
- pdfkit
- pytest
All dependencies are listed in [`requirements.txt`](./requirements.txt).

---

## 📁 About the Data

This is a **synthetic dataset** built for portfolio demonstration purposes. It simulates realistic data quality issues often encountered in freelance or corporate data projects.

---

## 👨‍💻 Author

**Gabor Barta**  
Aspiring Data Engineer | Python & Data Cleaning Enthusiast  
🔗 [LinkedIn](https://www.linkedin.com/in/gabor-barta-16a317210)  
🔗 [GitHub](https://github.com/your-bartagabor1)

---

## ⭐ Acknowledgements

- Project inspired by common freelance data tasks (e.g., Fiverr, Upwork)
- Focused on real-world data issues, automation, and reproducibility

---

## 🚀 Let’s Connect

Feel free to fork the repo, raise issues, or drop a message on LinkedIn.  
Thanks for checking out the project!
