# import requests

# r = requests.get("https://api.github.com")
# print(r.status_code)

from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws.append(["Name", "Age"])
ws.append(["Salah", 27])
ws.append(["Ahmed", 30])

wb.save("data.xlsx")














