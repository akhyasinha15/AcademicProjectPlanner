from data.db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(100))
    role = db.Column(db.String(20))  # student/admin


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_type = db.Column(db.String(20))
    team_size = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    technology = db.Column(db.String(50))


class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rule_type = db.Column(db.String(20))  # planning / architecture
    condition = db.Column(db.String(200))
    output = db.Column(db.String(200))