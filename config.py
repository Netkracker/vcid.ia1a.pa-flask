import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supergeheimespasswort")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "postgresql://postgres:Welcome$2025@localhost/nomnom")
    SQLALCHEMY_TRACK_MODIFICATIONS = False