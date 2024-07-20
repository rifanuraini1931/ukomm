from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Applicant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    nik = db.Column(db.String(20), nullable=False)
    whatsapp_number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    training_program = db.Column(db.String(50), nullable=False)
