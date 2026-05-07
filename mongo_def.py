from pymongo import MongoClient
from datetime import datetime


cliente = MongoClient("mongodb://127.0.0.1:27017/")
db = cliente["universidad"]
coleccion = db["estudiantes"]


