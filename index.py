from flask import Flask
from flask import render_template, request, redirect, url_for

import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="mysecretpassword",
    dbname = "product"
    )
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    table = cur.fetchall()
    list = []
    for x in table:
        list.append("<tr>")
        for y in range(3):
            list.append("<td>"+str(x[y])+"</td>")
        #list.append("<td><input type=number min=1 id="ST"></td>")
        list.append("</tr>")
    vysledny = " ".join(list)   


    return '''<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Online Shop</title>
<script 
	src="https://code.jquery.com/jquery-3.6.0.min.js"
      integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4="
      crossorigin="anonymous">
</script>
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>
<body>
<h2>Current products</h2>

<table>
  <tr>
    <th>Product</th>
    <th>Available</th>
    <th>Product Price</th>
    <th>Quantity</th>
  </tr>
  ''' + vysledny +'''
  <tr><td><input type=number min=0 id="ST" value=0></td></tr>
  <tr><td><input type=number min=0 id="SI" value=0></td></tr>
  <tr><td><input type=number min=0 id="KS" value=0></td></tr>
  <tr><td><input type=number min=0 id="KM" value=0></td></tr>
  <tr><td><input type=number min=0 id="AKU" value=0></td></tr>
</table><br>

<button type="button" onclick="buy()">Buy!</button>

<script>
var ST = $("#ST");
var SI = $("#SI");
var KS = $("#KS");
var KM = $("#KM");
var AKU = $("#AKU");

function buy(){       
     $.ajax({
		url:"http://127.0.0.1:5000/add",
		type:'POST',
		contentType: "application/json",
            data: JSON.stringify({"quantityST": ST.val(), "quantitySI": SI.val(), "quantityKS": KS.val(), "quantityKM": KM.val(), "quantityAKU": AKU.val()}),
		success: function(data){
			}
    });
    alert('You bought some products! Enjoy :)')
}

</script>

</body>
</html>
'''

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json(force=True)
    data_dict = dict(data)
    conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="mysecretpassword",
    dbname = "product"
    )
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("UPDATE products SET available=available - {} WHERE product = 'Skrutka tesárska 8,0×240'".format(data_dict['quantityST']))
    cur.execute("UPDATE products SET available=available - {} WHERE product = 'Skrutka imbus 6x40 Zn'".format(data_dict['quantitySI']))
    cur.execute("UPDATE products SET available=available - {} WHERE product = 'Klince stavebné 150x5'".format(data_dict['quantityKS']))
    cur.execute("UPDATE products SET available=available - {} WHERE product = 'Kladivo murárske 600g'".format(data_dict['quantityKM']))
    cur.execute("UPDATE products SET available=available - {} WHERE product = 'Aku vŕtačka Einhell TE'".format(data_dict['quantityAKU']))
    
    return "201"

@app.route("/connect")
def connect():
 connection = psycopg2.connect(dbname="product", user='postgres',
password='mysecretpassword', host='localhost')
 return "<h1 style='color:blue'>Connected!</h1>"

if __name__ == '__main__':
    app.run()
