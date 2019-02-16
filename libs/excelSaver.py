import pandas as pd
def save(dicts, filename):
    writer = pd.ExcelWriter(filename)
    for dict in dicts:
        dict['df'].to_excel(writer, dict['sheetName'])
    writer.save()

