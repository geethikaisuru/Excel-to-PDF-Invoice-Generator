import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("Excel-Data/*.xlsx")
# Load the data
for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    print(df)
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()  
    pdf.set_font("Arial", size=17, style="B")

    # get the invoice number from the file name
    invoice_number, date = (Path(filepath).stem).split("-")
    pdf.cell(200, 10, txt=f"Invoice Nu: {invoice_number}", ln=True, align="L")

    pdf.set_font("Arial", size=11)
    pdf.cell(200, 10, txt=f"Date: {date}", ln=True, align="L")

    # Add the  table from the excel file
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    # Add headers
    columns = list(df.columns)
    columns = [item.replace("_", " ").title() for item in columns]
    pdf.set_font("Arial", size=10, style="B")
    pdf.cell(30, 8, txt=columns[0], border=1)
    pdf.cell(70, 8, txt=columns[1], border=1)
    pdf.cell(40, 8, txt=columns[2], border=1)
    pdf.cell(30, 8, txt=columns[3], border=1)
    pdf.cell(30, 8, txt=columns[4], border=1, ln=1)


    # Add data
    for index, row in df.iterrows():
        pdf.set_font("Arial", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(30, 8, txt=str(row['product_id']), border=1)
        pdf.cell(70, 8, txt=str(row['product_name']), border=1)
        pdf.cell(40, 8, txt=str(row['amount_purchased']), border=1)
        pdf.cell(30, 8, txt=str(row['price_per_unit']), border=1)
        pdf.cell(30, 8, txt=str(row['total_price']), border=1, ln=1)


    # Add the total price
    total_price = df['total_price'].sum()

    pdf.cell(30, 8, txt="", border=1)
    pdf.cell(70, 8, txt="", border=1)
    pdf.cell(40, 8, txt="", border=1)
    pdf.cell(30, 8, txt="", border=1)
    pdf.cell(30, 8, txt=f"{total_pri  ce}", border=1, ln=1)
    
    # Add breaklines and the logo
    pdf.ln(3)
    pdf.image("logo.png", w=30)

    pdf.output(f"Invoices\{invoice_number}.pdf")