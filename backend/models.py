from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    ip = db.Column(db.String(15))
    api_user = db.Column(db.String(50))
    api_password = db.Column(db.String(100))
    snmp_user = db.Column(db.String(50))
    snmp_auth_pass = db.Column(db.String(100))
    snmp_enc_pass = db.Column(db.String(100))