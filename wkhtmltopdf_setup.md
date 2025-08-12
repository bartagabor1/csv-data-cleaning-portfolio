# wkhtmltopdf Setup Guide

This guide helps you install and configure `wkhtmltopdf` so that PDF reports can be generated successfully using `pdfkit` in this project.

---

## 🔧 What is `wkhtmltopdf`?

`wkhtmltopdf` is an open-source command-line tool that converts HTML files to PDFs using the WebKit rendering engine.  
It is required by `pdfkit` to generate PDF reports from HTML in this project.

---

## ✅ Installation Instructions (Windows)

1. Download the Windows installer from the official page:  
   👉 https://wkhtmltopdf.org/downloads.html

2. Choose the version under **"Windows (MSVC)"**, e.g.:  
   `wkhtmltopdf-0.12.6-1.msvc.exe`

3. Run the installer and install it to the default location:  
   `C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe`

---

## 🧠 Set Environment Variable

To allow your Python script to find `wkhtmltopdf`, add its path as a **user environment variable**.

### Steps:

1. Open **Start Menu** → search for **"Environment Variables"**
2. Click on **"Edit the system environment variables"**
3. In the window that opens, click **Environment Variables...**
4. Under **User variables**, click **New**
   - **Variable name**: `WKHTMLTOPDF_PATH`  
   - **Variable value**: `C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe`
5. Click OK → OK → OK
6. Restart your code editor or terminal so the environment variable takes effect.

---

## 🧪 Test Your Setup

You can test if the variable is set correctly by running this small Python snippet:

```python
import os
print("WKHTMLTOPDF_PATH =", os.getenv("WKHTMLTOPDF_PATH"))
```

You should see:

```
WKHTMLTOPDF_PATH = C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe
```

---

## 🐛 Troubleshooting

- **PDF not generating?**
  - Ensure the environment variable is set **as a user variable**, not system-wide (unless you know what you're doing).
  - Make sure the path is correct and points to `wkhtmltopdf.exe`.
  - Restart your terminal or editor after setting the variable.

- **Still not working?**  
  - You can also manually pass the path in code:

```python
import pdfkit
config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
pdfkit.from_file("input.html", "output.pdf", configuration=config)
```

---

## 🧼 Project Integration

In this project, the script looks for the path automatically via:

```python
wkhtmltopdf_path = os.getenv("WKHTMLTOPDF_PATH")
```

If found, it uses the path to configure `pdfkit`.  
If not found, it falls back to the system default.

---

✅ Once this is working, your pipeline will automatically generate PDF reports in the `/reports` folder.

---
