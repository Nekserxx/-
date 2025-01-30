from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker



app = Flask(__name__)
app.secret_key = 'qT6u5xM4hbGPFV8ZQyEdwg2eSUtYKsmaNH3zBpcALk9rvfD7JW'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.jorvdopwibsdpviawomq:teD8A8oJ0a66g6wy@aws-0-eu-central-2.pooler.supabase.com:6543/postgres'
db = SQLAlchemy(app)

engine = create_engine('postgresql://postgres.jorvdopwibsdpviawomq:teD8A8oJ0a66g6wy@aws-0-eu-central-2.pooler.supabase.com:6543/postgres')
db_e = scoped_session(sessionmaker(bind=engine))