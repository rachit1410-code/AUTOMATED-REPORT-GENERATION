# AUTOMATED-REPORT-GENERATION

COMPANY: CODTECH IT SOLUTIONS

NAME: RACHIT DUBEY

INTERN ID: CT08DG1287

DOMAIN: PYTHON PROGRAMMING

DURATION: 2 MONTH (8 WEEKS)

MENTOR: NEELA SANTOSH


#DISCRIPTION

# Automated PDF Sales Report Generator

This project is part of my internship task with *CODTECH*.  
The goal was to create a Python script that *reads sales data from a file, analyzes it, and generates a **formatted PDF report* using the ReportLab library.

---

## 📌 Features
- Reads sales data from a *CSV file*
- Automatically calculates:
  - Total sales per product
  - Grand total sales
  - Date range of sales data
- Generates a *well-formatted PDF report* with:
  - Title and meta information
  - Summary table of sales
- Automatically creates a *sample CSV file* if no data file is found
- Clean, modular, and easy-to-read code

---

## 📂 Project Structure
The project folder contains the following files and their purposes:-
# Main project folder │ report_project/          
# Input CSV file with sales data │ sales_data.csv                               
# (If missing, the script generates a sample automatically) │ report_generator.py          
# Main Python script that: │                                
# - Reads and analyzes sales data │                                
# - Calculates total sales per product │                                
# - Generates a formatted PDF report │ Monthly_Sales_Report.pdf     
# The final generated PDF report │ preview.png                  
# Screenshot preview of the generated PDF (for README) │ requirements.txt              
# List of required Python libraries (pandas, reportlab) │ README.md                     
# Project documentation
*Notes:*
- **sales_data.csv** → Your source data. Replace with your real dataset if needed.
- **report_generator.py** → The script to run in Python for generating the PDF.
- **Monthly_Sales_Report.pdf** → The output report.
- **requirements.txt** → Helps install dependencies quickly.
- **preview.png** → Optional, used for visual reference in README.

---

## 🛠 Technologies Used
- *Python 3.8+*
- [pandas](https://pandas.pydata.org/) – Data analysis
- [ReportLab](https://www.reportlab.com/) – PDF generation

---

## 📦 Installation

1. *Clone the repository*
```
git clone https://github.com/rachit1410-code/AUTOMATED-REPORT-GENERATION.git
cd AUTOMATED-REPORT-GENERATION
```
2.Create a virtual environment ( option but recommended)
```
python -m venv venv
```
3. Activate the virtual environment

-Windows (PowerShell)

```
venv\Scripts\Activate.ps1
```

-Windows (Command Prompt)

```
venv\Scripts\activate.bat
```
-macOS / Linux

```
source venv/bin/activate
```
4. Install dependencies
```
pip install pandas reportlab
```
---

▶ Usage

1. Make sure you have a CSV file named ```sales_data.csv``` in the project folder.
You can also let the script generate a sample dataset automatically.


2. Run the script:
```
python report_generator.py
```
3. The PDF report (```Monthly_Sales_Report.pdf```) will be created in the same folder.




---

📊 Sample CSV Format
```
Date,Product,Quantity,Price
2025-07-01,Apples,35,2.50
2025-07-01,Bananas,50,1.20
2025-07-01,Milk (1L),20,1.50
2025-07-02,Bread,15,1.00
2025-07-02,Oranges,40,3.00
```

---

📄 Sample Output

```Monthly_Sales_Report.pdf``` will include:

Report title

Date range and total sales info

A formatted table showing each product's total sales


---

📌 Notes

If ```sales_data.csv is missing```, the script automatically generates a sample dataset.

You can replace the sample CSV with your own data for real reports.



---

🖋 Author

[Rachit dubey ] – Internship Task for CODTECH
