import sys
sys.path.append("../site-packages")
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, flash , redirect, request
app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dpsmkCertificateData.db'
dab = SQLAlchemy(app)
