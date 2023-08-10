from fastapi import FastAPI
from src.settings import settings
from src.session import engine
from src.base_class import Base


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,
                  version=settings.PROJECT_VERSION)
    create_tables()
    return app


app = start_application()


@app.get("/")
def home():
    return {"msg": "Hello FastAPI🚀"}
