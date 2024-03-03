from lib_book import error_4
from lib_book import fetch

from flask import Flask, render_template, request
from jinja2 import Environment, FileSystemLoader, Template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def search():
    use = request.form['use']
    data_list = fetch.extract_data(use)
    if data_list != []:
        rows = ""
        for row in data_list:
            rows += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td><a href='{row[3]}'>Link</a></td><td><a href='{row[4]}'>Link</a></td></tr>"        
        temp = (
            """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
    <style>

body
{
    background-color: black;
    color: white;
    font-family: sans-serif;
    font-weight: 700;
}
#nav
{
    display:flex;
    flex-direction: row;
    justify-content:left;
    align-items: center;
    

}
#body
{
    display: flex;
    flex-direction: row;
    
}
#nav p
{
   
    font-family: sans-serif;
    margin-inline: 1%;
}
#nav input
{
    font-family: sans-serif;
    height: 50%;
}
#sidebar
{
    display: flex;
    flex-direction: column;
    justify-items: center;
   
    width:15%;
    background-color: rgb(43, 41, 41);
    border-radius: 10px;
    margin-right: .5%;
}

.sort
{
    display: flex;
    flex-direction: row;
    background-color:  black;
    margin-bottom: 5%;
    border-radius: 10px;
    padding: 1px;
    
    
}

.sort div p
{
    text-align: center;

    font-size: 80%;
    margin:0;
    width:80px;
    padding:5px;
    
    
}
.sort select
{
    height: 100%;
    background-color:  rgb(43, 41, 41);
    border-style: none;
    color: white;
    font-family: sans-serif;
    font-weight: 700;
    border-radius: 10px;
}
#search
{
    background-image: linear-gradient(red,rgb(43, 41, 41),rgb(43, 41, 41));
    display: flex;
    flex-direction: column;
    width:85%;
    height: 610px;
    align-items: center;
    justify-content: center;
    font-size: 30px;
    background-color: rgb(43, 41, 41);
    border-radius: 10px;
    
}
#search p
{
    margin:0;
    font-size: 50%;
    margin-bottom: 5%;
}

    
    
#main-body
{
    
    display: flex;
    flex-direction: row;
    height: 100%;
}

#footer
{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-items: center;
    
}
#footer-block
{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-items: center;
    margin: 1.5%;
}
#footer p
{
    margin:0;
}

#filter
{
    display: flex;
    flex-direction: column;
    margin:5%;

}
#search-act input
{
    color:white;
    font-size: 60%;
   background-color: black;
    border-style: none;
    border-radius: 15px;
    width: 400px;
    height: 100%;

}
#search-act button
{
    font-size: 60%;
    font-weight: 700;
    background-color:  rgb(34, 32, 32);
    border-style: none;
    color:white;
    border-radius: 15px;
    width: 100px;
    height:100%;
}
#reccomendation
{

    display:flex;
    flex-direction: row;
    justify-content: space-around;
    width:100%;
}
#reccomendation div
{
    
    background-color: black;
    height: 150px;
    width:100px;
    border-radius: 5px;
    

}
#search-act
{
    margin-bottom: 10%;
}

#Name
{
    font-size: 100px;
}


        table , th , td {
    border: 1px solid #ddd;
    background-image: linear-gradient(red,rgb(43, 41, 41),rgb(43, 41, 41));
    flex-direction: column;
    flex-direction: row;
    
}
table{
    width:100%;
}
th{
    text-align:center;
}
tr:nth-child(even){
    background-color:white;
}
    </style>
</head>
<body>
    <div id="nav">
        <p>Home</p>
        <p>About</p>
        <p>Discover</p>
    </div>
    <div id="main-body"></div>
        <div id="RESULTS">
            <h1>RESULTS<h1>
        </div>

        <br>
        <br>
        <div style="overflow-x:auto;">
        <table>
            <tr>
                <div>
                    <th>Name  </th>
                    <th>Author  </th>
                    <th>Language  </th>
                    <th>Link for text file  </th>
                    <th>Link for ebook  </th>
                </div>

            </tr>
            """+rows+"""""

        </table>
        </div>
    </div>
</body>
</html>
""" 
        )

        with open("output.html","w") as file:
            file.write(temp)
            return temp

    else:
        return "NO DATA FOUND!"
    

if __name__ == "__main__":
    app.run(debug=True)

    

