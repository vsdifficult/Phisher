from flask import Flask, render_template, request, redirect
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html>
  <head>
    <title>Мой сайт</title>
  </head>
  <body>
    <h1>Добро пожаловать на мой сайт!</h1>
    <a href="/register">Регистрация</a>
  </body>
</html>
"""

@app.route("/register/config") 
def main(): 
            return """
<!DOCTYPE html>
<html>

<head>
    <title>Окно входа</title>
    <style>
        body {
            background-color: #f2f2f2;
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }

        .container {
            width: 300px;
            margin: 100px auto;
            background-color: white;
            border: 1px solid #ccc;
            padding: 20px;
            text-align: center;
        }

        h1 {
            margin-top: 0;
        }

        input[type=text],
        input[type=password] {
            width: 100%;
            padding: 12px 20px;
            margin: 8px 0;
            display: inline-block;
            border: 1px solid #ccc;
            box-sizing: border-box;
        }

        button {
            background-color: #4CAF50;
            color: white;
            padding: 14px 20px;
            margin: 8px 0;
            border: none;
            cursor: pointer;
            width: 100%;
        }

        button:hover {
            opacity: 0.8;
        }
    </style>
</head>

<body>
    <div class="container">
        <h1>Регистрация</h1>
        
        
        <form method="post" action="/register">
            <input type="text" placeholder="Логин" name="username" required><br>
            <input type="password" placeholder="Пароль" name="password" required><br>
            <button type="submit">Войти</button>
        </form>
    </div>
</body>
</html>
"""

     


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        url = "http://127.0.0.1:8080"
        response = requests.get(url) 

        g = BeautifulSoup(response.text, "html.parser") 
        
        for i in g.find_all("type"):
            print(i) 

  
    else:
        
      
    
       return """
<!DOCTYPE html>
<html>

<head>
    <title>Окно входа</title>
    <style>
        body {
            background-color: #f2f2f2;
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }

        .container {
            width: 300px;
            margin: 100px auto;
            background-color: white;
            border: 1px solid #ccc;
            padding: 20px;
            text-align: center;
        }

        h1 {
            margin-top: 0;
        }

        input[type=text],
        input[type=password] {
            width: 100%;
            padding: 12px 20px;
            margin: 8px 0;
            display: inline-block;
            border: 1px solid #ccc;
            box-sizing: border-box;
        }

        button {
            background-color: #4CAF50;
            color: white;
            padding: 14px 20px;
            margin: 8px 0;
            border: none;
            cursor: pointer;
            width: 100%;
        }

        button:hover {
            opacity: 0.8;
        }
    </style>
</head>

<body>
    <div class="container">
        <h1>Регистрация</h1>
        <form action="register" method ="POST">
            <input type="text" placeholder="Логин" name="username" required><br>
            <input type="password" placeholder="Пароль" name="password" required><br>
            <button type="submit">Войти</button>
        </form>
    </div>
</body>
</html>
"""
   
    
if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port=8080) 

# /app_dir
#     /app
# 	__init__.py
# 	/static
# 	/templates
# 	views.py
#     config.py
#     runner.py