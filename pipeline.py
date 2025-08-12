import os
import pandas as pd
import pdfkit
from scripts.cleaning import clean_data

class DataCleaningPipeline:
    def __init__(self, raw_data_path, cleaned_data_path, report_dir="reports"):
        self.raw_data_path = raw_data_path
        self.cleaned_data_path = cleaned_data_path
        self.report_dir = report_dir
        os.makedirs(self.report_dir, exist_ok=True)
        os.makedirs(os.path.dirname(self.cleaned_data_path), exist_ok=True)

        wkhtmltopdf_path = os.getenv('WKHTMLTOPDF_PATH')
        if wkhtmltopdf_path:
            self.config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)
            print(f"✅ Using wkhtmltopdf path: {wkhtmltopdf_path}")
        else:
            self.config = None
            print("⚠️ No wkhtmltopdf path set. PDF export may fail.")

    def load_data(self):
        print("📥 Loading raw data...")
        self.raw_df = pd.read_csv(self.raw_data_path)

    def generate_report(self, df, report_name):
        html_path = os.path.join(self.report_dir, f"{report_name}_simple_report.html")
        pdf_path = os.path.join(self.report_dir, f"{report_name}_simple_report.pdf")
        desc = df.describe(include='all').to_html()

        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(f"<h1>Simple Data Report - {report_name}</h1>")
            f.write(desc)

        print(f"✅ HTML report saved to: {html_path}")
        try:
            if self.config:
                pdfkit.from_file(html_path, pdf_path, configuration=self.config)
            else:
                pdfkit.from_file(html_path, pdf_path)
            print(f"📄 PDF report saved to: {pdf_path}")
        except Exception as e:
            print(f"⚠️ PDF generation failed: {e}")

    def clean_data(self):
        print("🧼 Cleaning data...")
        self.cleaned_df = clean_data(self.raw_df)

    def save_cleaned_data(self):
        print("💾 Saving cleaned data...")
        self.cleaned_df.to_csv(self.cleaned_data_path, index=False)

    def run(self):
        self.load_data()
        self.generate_report(self.raw_df, "raw_data")
        self.clean_data()
        self.save_cleaned_data()
        self.generate_report(self.cleaned_df, "cleaned_data")
        print("✅ Pipeline complete.")

# Optional: example usage if needed
if __name__ == "__main__":
    pipeline = DataCleaningPipeline(
        raw_data_path="sample_data/messy_data.csv",
        cleaned_data_path="outputs/cleaned_data.csv"
    )
    pipeline.run()
