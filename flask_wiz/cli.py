import os
import click
from flask import Flask

db_options = {'1':'mongodb', '2':'sqlite3', '3':'mysql', '4':'postgresql'}
value_key = {v: k for k,v in db_options.items()} #created reverse mapping of values to keys

#to display options
def display_options():
    options = "\n".join([f"{key}: {value}" for key, value in db_options.items()])
    return f"Select database system:\n{options}\n(Enter either key or value)" 

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Namaste Duniya! This is a Flask app generated by Flask-Wiz.'

    return app

@click.group()
def cli():
    pass

@cli.command()
def new():
    name = click.prompt('Enter project name')

    click.echo(display_options())
    db_input = click.prompt('db selection')

    if db_input in db_options:
        db_key = db_input
    elif db_input in value_key:
        db_key = value_key[db_input]
    else:
        click.echo('Invalid input')
        return

    os.makedirs(name)
    os.chdir(name)

    os.makedirs('templates')
    os.chdir('templates')

    with open('home.html', 'w') as home_file:
        home_file.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask-app</title>
</head>
<body>
    <h1>flask app generated with flask-wiz</h1>
    <p>{{ message }}</p>
</body>
</html>""")

    os.chdir('..')

    os.makedirs('static')
    os.chdir('static')

    os.makedirs('css')
    os.makedirs('js')
    os.makedirs('img')
    os.chdir('..')

    with open('.gitignore', 'w') as gitignore_file:
        gitignore_file.write("# Default .gitignore for Flask project\n")
        gitignore_file.write("venv/\n")
        gitignore_file.write("__pycache__/\n")
        gitignore_file.write(".vscode/\n")

    with open('.env', 'w') as env_file:
        env_file.write("# Default .env file for Flask project\n")

    with open('app.py', 'w') as app_file:
        db_module = None

        match db_key:
            case '1':
                db_module = 'pymongo'
                app_file.write(
                """from flask import Flask, render_template, redirect
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['my_database']

@app.route('/')
def index():
    return render_template('home.html', message = 'Namaste Duniya! This is a Flask app generated by Flask-Wiz for MongoDB.')

if __name__ == '__main__':
    app.run()
""")
            case '2':
                db_module = 'sqlite3'
                app_file.write(
                """from flask import Flask, render_template, redirect
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('database.db')

@app.route('/')
def index():
    return render_template('home.html', message = 'Namaste Duniya! This is a Flask app generated by Flask-Wiz for SQLite.')

if __name__ == '__main__':
    app.run()
""")
            case '3':
                db_module = 'pymysql'
                app_file.write(
                """from flask import Flask, render_template, redirect
import pymysql

app = Flask(__name__)
conn = pymysql.connect(host='localhost', user='root', password='', database='my_database')

@app.route('/')
def index():
    return render_template('home.html', message = 'Namaste Duniya! This is a Flask app generated by Flask-Wiz MySQL.')

if __name__ == '__main__':
    app.run()
""")
            case '4':
                db_module = 'psycopg2'
                app_file.write(
                """from flask import Flask, render_template, redirect
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(host='localhost', user='postgres', password='', dbname='my_database')

@app.route('/')
def index():
    return render_template('home.html', message = 'Namaste Duniya! This is a Flask app generated by Flask-Wiz PostgreSQL.')

if __name__ == '__main__':
    app.run()
""")
            case _:
                print('Invalid choice. Please choose a valid database system.')

    if db_module:
        os.system("pip install flask")
        
        if db_module != 'sqlite3':
            os.system(f"pip install {db_module}")  # Install the required database module

        # to create a requirements file
        os.system(f"pip freeze > requirements.txt")

    click.echo(f'New Flask project "{name}" created successfully with {db_module} database!')

if __name__ == '__main__':
    cli()