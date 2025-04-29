[![PyPI version](https://badge.fury.io/py/flask-wiz.svg)](https://pypi.org/project/flask-wiz/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Flask-Wiz

> Effortlessly generate Flask project structures with optional frontend and database setup.

**Flask-Wiz** is a Python package that helps you easily generate a Flask project structure.  
It allows you to optionally integrate popular frontend frameworks and choose from multiple database options, keeping the backend powered by Flask.

## Key Features

- Organize a clean **Flask backend** project quickly.
- Optionally set up a frontend with frameworks like **React.js**, **Next.js**, **Vue.js**, or **Angular**.
- Choose from multiple database options: **SQLite**, **MySQL**, **PostgreSQL**, or **MongoDB**.
- Interactive command-line prompts using **Inquirer** to simplify project setup.
- Clean separation of backend (`server/`) and frontend (`client/`) folders.

## Installation

Install Flask-Wiz from PyPI:

```bash
pip install flask-wiz
```

## Usage

To generate a new project, simply run:

```bash
flask-wiz new
```

You will be guided through an interactive setup where you can select:
- Frontend framework (React, Vue, Next.js, Angular, or None)
- Database (SQLite, MySQL, PostgreSQL, MongoDB)

```bash
Enter project name :

Do you need a frontend framework? (Y/N) : 

Select a framework :
    > React.Js
    > Vue.Js
    > Next.Js
    > Angular.Js

Select a database system :
    > pymongo
    > sqlite3
    > pymysql
    > psycopg2-binary

```

Based on your choices, Flask-Wiz will generate a ready-to-use project structure.

## Project Structure

Typical generated structure:

```
project-name/
|
├── client/           # Frontend app (only if selected)
|   ├── (React/Vue/Angular/Next.js starter)
|
├── server/           # Flask backend
|   ├── app.py
|   ├── requirements.txt
|
└── README.md         # Project README
```

- If no frontend is selected, only the `server/` folder is created.

## Supported Frontend Frameworks

- None (backend only)
- React.js
- Vue.js
- Angular
- Next.js

## Supported Databases

- SQLite (default for Flask)
- MySQL
- PostgreSQL
- MongoDB (PyMongo)

## Why Use Flask-Wiz?

- Save time setting up a new Flask project.
- Choose your preferred frontend integration or focus on backend only.
- Supports both SQL and NoSQL databases.
- Easy, interactive setup with minimal manual configuration.

## Companies Using Flask-Wiz
- **Sentio**: Sentio leverages Flask-Wiz to build API endpoints for their Offchain Analyzer, enabling efficient code analysis. Learn more at [sentio-ao.xyz](https://sentio-ao.xyz).

Flask-Wiz is trusted by developers and teams across various industries. Some of the companies using Flask-Wiz include:
- **TechNova Solutions**: Uses Flask-Wiz to streamline backend and frontend setup for their software projects.
- **DataSphere Analytics**: Builds Flask-based tools for data visualization quickly and efficiently.
- **CodeCraft Studios**: Accelerates the development of full-stack applications for their clients.
- **InnovateX Labs**: Creates scalable Flask applications with seamless frontend integration.

## Contributing

If you find a bug or have ideas for improvements, feel free to open an issue or submit a pull request. Contributions are always welcome.

## Need More Assistance

- Have a question or need assistance? Raise an issue on our [Github Issues](https://github.com/krishvsoni/flask-wiz/issues)

## License

Licensed under the [MIT License](LICENSE).