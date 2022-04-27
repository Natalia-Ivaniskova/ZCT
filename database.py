import psycopg2

conn = psycopg2.connect(host="seconddb.c6w5z1fwdsy4.eu-central-1.rds.amazonaws.com", user = "seconduser", password="secondpassword", dbname= "seconddb")
conn.autocommit = True
cur = conn.cursor()
cur.execute("CREATE TABLE products (Product VARCHAR(200), Available INT, Product_Price VARCHAR(20))")
cur.execute("INSERT into products (Product, Available, Product_Price) values ('Skrutka tesárska 8,0×240', 350, '4,50€/kg')")
cur.execute("INSERT into products (Product, Available, Product_Price) values ('Skrutka imbus 6x40 Zn', 200, '3€/kg')")
cur.execute("INSERT into products (Product, Available, Product_Price) values ('Klince stavebné 150x5', 450, '3€/kg')")
cur.execute("INSERT into products (Product, Available, Product_Price) values ('Kladivo murárske 600g', 20, '6€/ks')")
cur.execute("INSERT into products (Product, Available, Product_Price) values ('Aku vŕtačka Einhell TE', 15, '47€/ks')")

print("WRITTEN INTO")
