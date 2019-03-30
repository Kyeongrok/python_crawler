import pandas as pd

def save(df, filename):
    writer = pd.ExcelWriter(filename)
    df.to_excel(writer, "sheet1")
    writer.save()
