# main.py

from fastapi import FastAPI
from configparser import ConfigParser


parser = ConfigParser()
parser.read('settings.ini')


app = FastAPI(title=parser.get('project_credentials', 'project_name'),
              version=parser.get('project_credentials', 'project_version'))


@app.get("/")
def hello_api():
    return {"msg": "Hello FastAPI🚀"}
