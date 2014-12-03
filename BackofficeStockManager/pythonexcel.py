import xlwt
import mysql.connector

config = {
  'user': 'root',
  'password': '',
  'host': '127.0.0.1',
  'database': 'login_test',
  'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

query = ("SELECT name, ref, brand, stock_stock.desc, price, stock FROM stock_stock ")
cursor.execute(query)

book = xlwt.Workbook()
sheet1 = book.add_sheet("Sheet 1")
sheet1.write(0,0,'Nome')
sheet1.write(0,1,'Ref')
sheet1.write(0,2,'Marca')
sheet1.write(0,3,'Desc')
sheet1.write(0,4,'Preco')
sheet1.write(0,5,'Stock')
linha=1
for (name, ref, brand, desc, price, stock) in cursor:
	sheet1.write(linha,0,name)
	sheet1.write(linha,1,ref)
	sheet1.write(linha,2,brand)
	sheet1.write(linha,3,desc)
	sheet1.write(linha,4,price)
	sheet1.write(linha,5,stock)
	linha=linha+1


book.save("stock.xls")
