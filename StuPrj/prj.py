from fpdf import FPDF
from pathlib import Path
import glob
import pandas as pd


# Load the .txt files data located inside the prj folder
filepaths = glob.glob("prj/*.txt")
for filepath in filepaths:
    with open(filepath, "r") as file:
        data = file.read()
        # print(data)
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()  
        pdf.set_font("Times", size=17, style="B")

        # Get the file name without the extension
        file_name = Path(filepath).stem
        pdf.cell(200, 10, txt=f"File Name: {file_name}", ln=True, align="L")

        # read the txt files and get the data inside it
        pdf.set_font("Times", size=11)
        pdf.add_dynamic_multicell(data, 200)
        #pdf.multi_cell(200, 40, txt=f"Data: {data}", align="L")
        pdf.output(f"prj\output\{file_name}.pdf")