# 🧼 Cleaning Summary – Messy Customer Data

**Project Name:** Customer Data Cleaning Portfolio  
**Data Source:** `sample_data/messy_data.csv`  
**Objective:** To clean and preprocess a realistic, messy customer dataset for further analysis or business reporting.

---

## ✅ Key Cleaning Steps

| Step | Description |
|------|-------------|
| 🧹 **Removed Duplicate Rows** | Identified and dropped 3 exact duplicate records using `drop_duplicates()` |
| 👤 **Filtered Invalid Names** | Removed rows where the `Name` field was missing or consisted only of whitespace |
| 📧 **Validated Email Addresses** | Standardized and validated emails using regex. Invalid formats were replaced with `NaN` |
| 🔢 **Converted and Imputed Age** | Converted the `Age` column to numeric, filled missing values with the median (29), and rounded to integers |
| 🌍 **Standardized Country Names** | Mapped inconsistent values like `"usa"` or `"UK"` to proper forms: `"United States"`, `"United Kingdom"` |
| 📅 **Parsed Sign-up Dates** | Converted sign-up dates to standard datetime format with `pd.to_datetime()` |
| 💰 **Cleaned Income Field** | Removed currency symbols, text, and commas. Converted to numeric, dropped negatives, and rounded to integer |
| 📌 **Normalized Status Values** | Trimmed whitespace, capitalized first letters, and filled missing values with `"Unknown"` |

---

## 📊 Dataset Overview

- **Input file:** `sample_data/messy_data.csv`  
  → Synthetic dataset containing **60** rows with common real-world data issues.
  
- **Output file:** `outputs/cleaned_data.csv`  
  → Cleaned and well-structured dataset with **[insert final row count here]** rows, ready for EDA, visualization, or reporting.

---

## 🛠️ Tools & Technologies Used

- **Python 3.10+**
- **Pandas** – data manipulation
- **NumPy** – numerical operations
- **Regex (`re`)** – pattern validation for email addresses
- **`os` module** – file path management

---

## 📁 Repository Contents

| File | Description |
|------|-------------|
| `scripts/clean_data.py` | Main cleaning script for preprocessing the raw dataset |
| `outputs/cleaned_data.csv` | The final cleaned data file |
| `sample_data/messy_data.csv` | The raw input data (simulated, messy) |
| `notebooks/eda.ipynb` *(optional)* | Exploratory data analysis notebook for profiling the cleaned dataset |
| `README.md` | Project overview and instructions |
| `cleaning_summary.md` | This summary of the data cleaning steps |

---

## 📌 Purpose

This project was built to demonstrate **practical data cleaning techniques** using Python and Pandas. The dataset was intentionally designed to include realistic data issues such as:

- inconsistent formatting  
- invalid or missing values  
- mixed data types  
- duplicate records

It’s ideal for showcasing end-to-end data preparation skills in a professional portfolio or client work (e.g. Fiverr, Upwork).

---

## 🙋‍♂️ Questions or Feedback?

Feel free to connect or open an issue.  
🔗 **[LinkedIn](https://www.linkedin.com/in/gabor-barta-16a317210)**  
🔗 **[GitHub](https://github.com/your-bartagabor1)**
Thanks for stopping by! 🚀
