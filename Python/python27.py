# // python script for generating continupus dates in excel
# // python script for date range between two values?
from datetime import date, timedelta
from openpyxl import load_workbook

start_date = date(2022, 8, 1) 
end_date = date(2022, 9, 1)    # perhaps date.now()

delta = end_date - start_date   # returns timedelta
res = []
for i in range(delta.days + 1):
    day = start_date + timedelta(days=i)
    res.append(day)

workbook_name = 'data.xlsx'
wb = load_workbook(workbook_name)
page = wb.active

# New data to write:
new_companies = [res]

for info in new_companies:
    page.append(info)

wb.save(filename=workbook_name)

# // python script for adding date to excel rows?