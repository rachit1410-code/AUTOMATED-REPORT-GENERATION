# Automated PDF Sales Report Generator
# Created by: [Rachit Dubey]
# Description: Reads sales data from CSV, analyzes it, and creates a formatted PDF report.

import os
import pandas as pd
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# File names
DATA_FILE = "sales_data.csv"
OUTPUT_FILE = "Monthly_Sales_Report.pdf"

# ------------------------------------------------------
# Step 1: Create a sample CSV if one doesn't exist
# ------------------------------------------------------
if not os.path.exists(DATA_FILE):
    sample_data = [
        ["Date", "Product", "Quantity", "Price"],
        ["2025-07-01", "Apples", 35, 2.50],
        ["2025-07-01", "Bananas", 50, 1.20],
        ["2025-07-01", "Milk (1L)", 20, 1.50],
        ["2025-07-02", "Bread", 15, 1.00],
        ["2025-07-02", "Oranges", 40, 3.00]
    ]
    pd.DataFrame(sample_data[1:], columns=sample_data[0]).to_csv(DATA_FILE, index=False)
    print(f"No CSV found. Created a sample file: {DATA_FILE}")

# ------------------------------------------------------
# Step 2: Read and process the data
# ------------------------------------------------------
df = pd.read_csv(DATA_FILE, parse_dates=["Date"])
df["Total"] = df["Quantity"] * df["Price"]

# Summary by product
product_summary = df.groupby("Product", as_index=False)["Total"].sum()
grand_total = df["Total"].sum()

# Date range for the report
date_from = df["Date"].min().date()
date_to = df["Date"].max().date()

# ------------------------------------------------------
# Step 3: Create PDF report
# ------------------------------------------------------
doc = SimpleDocTemplate(
    OUTPUT_FILE, 
    pagesize=A4, 
    rightMargin=30, 
    leftMargin=30, 
    topMargin=30, 
    bottomMargin=18
)

styles = getSampleStyleSheet()
content = []

# Report Title
content.append(Paragraph("Monthly Sales Report", styles["Title"]))
content.append(Spacer(1, 12))

# Report Meta Info
meta_info = f"""
<b>Report Generated:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}<br/>
<b>Data Range:</b> {date_from} to {date_to}<br/>
<b>Grand Total Sales:</b> ${grand_total:,.2f}
"""
content.append(Paragraph(meta_info, styles["Normal"]))
content.append(Spacer(1, 12))

# Sales Summary Table
table_data = [["Product", "Total Sales (USD)"]]
for _, row in product_summary.iterrows():
    table_data.append([row["Product"], f"${row['Total']:.2f}"])

table = Table(table_data, colWidths=[200, 150])
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#4B8BBE")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),
    ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
]))
content.append(table)

# Build PDF
doc.build(content)

print(f"✅ Report created successfully: {OUTPUT_FILE}")
