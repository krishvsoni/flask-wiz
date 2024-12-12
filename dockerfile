FROM python:3.9

WORKDIR /

COPY . flask-wiz/
COPY . setup.py
COPY . wiz.py
COPY . build/
COPY . dist/
COPY . flask_wiz/
COPY . flask_wiz.egg-info
COPY requirements.txt .


RUN pip install flask-wiz

EXPOSE 5000

CMD ["python", "wiz.py", "new", "--name", "your_project_name", "--db", "your_database_option"]
