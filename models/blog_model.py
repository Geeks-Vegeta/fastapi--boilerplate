from mongoengine import connect, Document, ListField, StringField, DateTimeField
from mongoengine.connection import disconnect
import os
from dotenv import load_dotenv 
import datetime

load_dotenv()

connect(host=os.getenv("MONGODB_URI"))


class Blog(Document):
    title = StringField(required=True, max_length=70)
    body = StringField(required=True, max_length=100)
    tags = ListField(required=True)
    created_at = DateTimeField(default=datetime.datetime.utcnow)
    updated_at = DateTimeField(default=datetime.datetime.utcnow)


    
disconnect(alias='some_alias')
