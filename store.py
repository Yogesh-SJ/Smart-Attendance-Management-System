import pandas as pd


with open('attendance.json', 'r') as f:
    attendance_log = json.load(f)


df = pd.DataFrame(attendance_log)


writer = pd.ExcelWriter('attendance_log.xlsx')
df.to_excel(writer, index=False)
writer.save()

