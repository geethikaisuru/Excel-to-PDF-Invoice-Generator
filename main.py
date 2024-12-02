import pandas as pd
import glob


filepaths = glob.glob("Excel-Data/*.xlsx")

# Load the data
for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    print(df)