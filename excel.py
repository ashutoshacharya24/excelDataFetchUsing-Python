import xlrd

wb=xlrd.open_workbook("E:\\yp\\Abc.xls")
ws=wb.sheet_by_name("Sheet1")

row_len=ws.nrows
col_len=ws.ncols

col_data=[]
row_data=[]
required_data=[]

for c in range(col_len):
    col_data.append(ws.cell(0, c).value)
for n in range(row_len):
    row_data.append(ws.cell(n,0).value)

while("" in col_data):
    col_data.remove("")
while("" in row_data):
    row_data.remove("")

def req_data():
    while("" in required_data):
        required_data.remove("")
    print("Values are : ",end="")
    print(required_data)

id=None
user=input("enter key to fetch data : ")

def GetData_By_ColumnName(user):
    if user in col_data:
        print("key exists !")
        id=col_data.index(user)
    for r in range(row_len):
        r2 = ws.cell(r, id).value
        required_data.append(r2)
    req_data()

def GetData_By_RowName(user):
    user=float(user)
    if user in row_data:
        print("key exists !")
        id=row_data.index(user)
    for c in range(col_len):
        c2=ws.cell(id,c).value
        required_data.append(c2)
    req_data()

def FetchData_By_Column_OR_Row_Name():
    if user in col_data:
        GetData_By_ColumnName(user)
    else:
        GetData_By_RowName(user)

FetchData_By_Column_OR_Row_Name()