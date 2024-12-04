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
    pdf.set_font("Times", size=17, style="B")

    # get the invoice number from the file name
    invoice_number, date = (Path(filepath).stem).split("-")
    pdf.cell(200, 10, txt=f"Invoice Nu: {invoice_number}", ln=True, align="L")

    pdf.set_font("Times", size=1
    )
    pdf.cell(200, 10, txt=f"Date: {date}", ln=True, align="L")
    pdf.output(f"Invoices\{invoice_number}.pdf")