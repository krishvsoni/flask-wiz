import os
import click
import inquirer
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from typing import List, Dict, Any
import subprocess

db_options = ['pymongo', 'sqlite3', 'pymysql','psycopg2-binary']
frontend_options = ['React.Js', 'Vue.Js', 'Next.Js', 'Angular.Js']

def display_options(message: str, choices: List[str]) -> str:
    """
    Presents an interactive List of options to the user.

    Args:
        message (str): The message to display to the user.
        choices (dict): A dictionary of options to display.
    
    Returns:
        str: The selected option or None if the user cancels.
    """

    questions = [
        inquirer.List('option',
                      message=message,
                      choices=choices),
    ]
    answers = inquirer.prompt(questions)
    if answers and 'option' in answers:
        return answers['option']
    return None


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db.init_app(app)
    return app

@click.group()
def cli():
    pass

@cli.command()
def new():
    while True:
        name = click.prompt('Enter project name')
        if os.path.exists(name):
            click.echo(f"Project {name} already exists. Choose another name.")
        else:
            break
    
    frontend_choice = click.confirm("Do you need a frontend framework?")
    
    if frontend_choice:
        frontend_framework = display_options("Select a framework:", frontend_options)
    else: 
        frontend_framework = None

    db_module = display_options("Select a database system:", db_options)
    
    os.makedirs(name)
    os.chdir(name)
    
    # Create server directory and setup backend
    os.makedirs('server')
    os.chdir('server')
    
    db_uri = ""

    if db_module == 'pymongo' :
        db_uri = "'mongodb://localhost:27017/my_database'"
    elif db_module == 'sqlite3' :
        db_uri = "'sqlite:///database.db'"
    elif db_module == 'pymysql' :
        db_uri = "'mysql+pymysql://root:password@localhost/my_database'"
    elif db_module == 'psycopg2-binary' :
        db_uri = "'postgresql://postgres:password@localhost/my_database'"
    
    with open('app.py', 'w') as app_file:
        if db_module == 'pymongo':
            app_file.write(f"""
from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)
mongo_uri = {db_uri}
client = MongoClient(mongo_uri)
db = client.get_default_database()

@app.route('/')
def index():
    return "Welcome to the Flask app!"

if __name__ == '__main__':
    app.run()
""")
            
        else:
            app_file.write(f"""
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = {db_uri}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return "Welcome to the Flask app!"

if __name__ == '__main__':
    app.run()
""")
    
    with open('requirements.txt', 'w') as req_file:
        req_file.write("flask\nflask_sqlalchemy\nflask_migrate\ngunicorn\n")
        if db_module and db_module != 'sqlite3':
            req_file.write(f"{db_module}\n")
    
    os.chdir('..')

    with open('README.md', 'w') as readme_file:
        readme_file.write(f"# {name}\n\nThis is a Flask project with {db_module} as the database.\n")

    if frontend_framework:
        os.makedirs('client')
        os.chdir('client')
        click.echo(f"Setting up {frontend_framework}...")
        if frontend_framework == 'React.Js':
            subprocess.run(["npm", "create", "vite@latest", ".", "--", "--template", "react"], shell=True, check=True)
        elif frontend_framework == 'Vue.Js':
            subprocess.run(["npm", "create", "vite@latest", ".", "--", "--template", "vue"], shell=True, check=True)
        elif frontend_framework == 'Next.Js':
            subprocess.run(["npx", "create-next-app@latest", "."], shell=True, check=True)
        elif frontend_framework == 'Angular.Js':
            try:
                subprocess.run(["ng", "--version"], shell=True, check=True)
            except subprocess.CalledProcessError:
                click.echo("Angular CLI is not found. Installing globally...")
                subprocess.run(["npm", "install", "-g", "@angular/cli"], shell=True, check=True)
            
            os.chdir('..')
            os.removedirs("client")
            subprocess.run(["ng", "new", "client"], shell=True, check=True)

        click.echo(f"{frontend_framework} setup complete.")
        os.chdir('..')

    click.echo(f"Project {name} created successfully!")
    click.echo("\nTo start the server, run:")
    click.echo(f"""\ncd {name}/server
pip install -r .\\requirements.txt
python app.py""")
    if frontend_framework:
        click.echo(f"\nTo start the client, run:")
        click.echo(f"""\ncd {name}/client
npm install
npm run dev""")


if __name__ == '__main__':
    cli()