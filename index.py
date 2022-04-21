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
        list.append("<tr></tr>")
        for y in range(3):
            list.append("<td>"+str(x[y])+"</td>")
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
</table><br>

<button type="button" onclick="buy()">Buy!</button>

<script>
var ST = $("#ST");
var SI = $("#SI");
var KS = $("#KS");
var KM = $("#KM");
var AKU = $("#AKU");

function buy(){
	alert('Hello world!')       
         }

</script>

</body>
</html>
'''

if __name__ == '__main__':
    app.run()