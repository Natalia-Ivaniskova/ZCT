from flask import Flask
from flask import render_template, request, redirect, url_for

import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
   return ''' 
<!DOCTYPE html>
<html>
<head>
    <style>
        nav{
            width: 100%;
            height: 80px;
            background-color: rgba(255,255,255,0.8);
            line-height: 80px;
        }

        nav ul{
            float: right; margin-right: 100px;
        }

        nav ul li{
            list-style-type: none;
            display: inline-block;
            padding: 0 40px;
            text-transform: uppercase;
        }

        nav ul li a{
            text-decoration: none;
            color: black;
            padding: 30px;
        }

        nav a:hover{
            color: white;
        }

        nav ul li:hover{
            background-color: black; transition: .3s;
        }

        *{
            margin: 0;
            padding: 0;
            font-family: Verdana;
        }

        #main{
            width: 100%;
            height: 100vh;
            background-size: cover;
            background-image: url("https://th.bing.com/th/id/R.8b5e90eb677f2dfc3bc745fab6d864e2?rik=tkrHeiegcznmwQ&pid=ImgRaw&r=0&sres=1&sresct=1");
        }

        .sitebackground h1{
            transform: translate(-50%, -50%); top: 50%; left: 50%; position: absolute;
            border: 3px solid whitesmoke; letter-spacing: 2px;
            padding: 2rem 8rem; text-align: center; color: whitesmoke;
        }

    </style>
</head>
<body>

<div id="main">
    <nav>
        <img src="1.png" width="150" height="80" alt="?">
        <ul>
            <li><a href=>Home</a></li>
            <li><a href=Products>Products</a></li>
            <li><a href=Contact>Contact</a></li>
        </ul>
    </nav>
</div>

<div class="sitebackground">
    <h1>CARPENTER E-SHOP</h1>
</div>

</body>
</html>
'''

@app.route('/Products')
def Products():
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
    a = 0
    list = []
    for x in table:
        a += 1
        list.append("<tr>")
        for y in range(3):
            list.append("<td>"+str(x[y])+"</td>")
        if a == 1:
            list.append("<td><input type=number min=0 id="+"ST"+" value=0></td>")
        elif a == 2:
            list.append("<td><input type=number min=0 id="+"SI"+" value=0></td>")
        elif a == 3:
            list.append("<td><input type=number min=0 id="+"KS"+" value=0></td>")
        elif a == 4:
            list.append("<td><input type=number min=0 id="+"KM"+" value=0></td>")
        elif a == 5:
            list.append("<td><input type=number min=0 id="+"AKU"+" value=0></td>")
        
        list.append("</tr>")
    vysledny = " ".join(list)   

    return '''<!DOCTYPE html>
<html>
<head>
    <script
            src="https://code.jquery.com/jquery-3.6.0.min.js"
            integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4="
            crossorigin="anonymous">
        </script>
    <style>

        table {
            font-family: sans-serif;
            border-collapse: collapse;
            margin: auto;
            width: 80%;
        }

        td, th {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }

        tr{
            background-color: rgba(255,255,255,0.8);
        }

        nav{
            width: 100%;
            height: 80px;
            background-color: rgba(255,255,255,0.8);
            line-height: 80px;
        }

        nav ul{
            float: right; margin-right: 100px;
        }

        nav ul li{
            list-style-type: none;
            display: inline-block;
            padding: 0 40px;
            text-transform: uppercase;
        }

        nav ul li a{
            text-decoration: none;
            color: black;
            padding: 30px;
        }

        nav a:hover{
            color: white;
        }

        nav ul li:hover{
            background-color: black; transition: .3s;
        }

        *{
            margin: 0;
            padding: 0;
            font-family: Verdana;
        }

        #main{
            width: 100%;
            height: 100vh;
            background-size: cover;
            background-image: url("https://th.bing.com/th/id/R.8b5e90eb677f2dfc3bc745fab6d864e2?rik=tkrHeiegcznmwQ&pid=ImgRaw&r=0&sres=1&sresct=1");
        }

        .sitebackground table{
            transform: translate(-50%, -50%); top: 50%; left: 50%; position: absolute;
            letter-spacing: 2px;
            padding: 2rem 8rem; text-align: center; color: black; width: 80%;
        }

        .sitebackground button{
            position: absolute;
            transform: translate(-50%, -50%); top: 75%; left: 50%;
            background-color: rgba(255,255,255,0.8);
            color: black; border: 3px solid black;
            width: 100px; height: 5vh;
        }


        button:hover{
            cursor: pointer;
            background-color: black;
            color: white;
            transition: .3s;
        }
    </style>
</head>
<body>

<div id="main">
    <nav>
        <img src="/img/pixil-frame-0.png" width="150" height="80" alt="?">
        <ul>
            <li><a href=/>Home</a></li>
            <li><a href=Products>Products</a></li>
            <li><a href=Contact>Contact</a></li>
        </ul>
    </nav>
</div>

<div class="sitebackground">
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
</div>

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

@app.route('/Contact')
def Contact():
    return'''
    <!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.13.1/css/all.min.css">
    <style>

        table {
            font-family: sans-serif;
            border-collapse: collapse;
            margin: auto;
            width: 80%;
        }

        td, th {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }

        tr{
            background-color: rgba(255,255,255,0.8);
        }

        nav{
            width: 100%;
            height: 80px;
            background-color: rgba(255,255,255,0.8);
            line-height: 80px;
        }

        nav ul{
            float: right; margin-right: 100px;
        }

        nav ul li{
            list-style-type: none;
            display: inline-block;
            padding: 0 40px;
            text-transform: uppercase;
        }

        nav ul li a{
            text-decoration: none;
            color: black;
            padding: 30px;
        }

        nav a:hover{
            color: white;
        }

        nav ul li:hover{
            background-color: black; transition: .3s;
        }

        *{
            margin: 0;
            padding: 0;
            font-family: Verdana;
        }

        #main{
            width: 100%;
            height: 100vh;
            background-size: cover;
            background-image: url("https://th.bing.com/th/id/R.8b5e90eb677f2dfc3bc745fab6d864e2?rik=tkrHeiegcznmwQ&pid=ImgRaw&r=0&sres=1&sresct=1");
        }

        .sitebackground{
            background-color: rgba(255,255,255,0.8);
            transform: translate(-50%, -50%); top: 50%; left: 50%;
            position: absolute;
            width: 30%;
            padding: 50px;
            text-align: center;
        }

        .sitebackground div{
            padding: 10px;
        }

    </style>
</head>
<body>

<div id="main">
    <nav>
        <img src="/img/pixil-frame-0.png" width="150" height="80" alt="?">
        <ul>
            <li><a href=/>Home</a></li>
            <li><a href=Products>Products</a></li>
            <li><a href=Contact>Contact</a></li>
        </ul>
    </nav>
</div>



<div class="sitebackground">
    <div><i class="fas fa-map-marker-alt"></i> Letná 1/9; 042 00 Košice-Sever; Slovakia</div>
    <div><i class="fas fa-envelope"></i> michal.ilek@student.tuke.sk</div>
    <div><i class="fas fa-envelope"></i> natalia.ivaniskova@student.tuke.sk</div>
</div>

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
