from data.db import db
from data.models import Rule

def add_rule(rule_type, condition, output):
    rule = Rule(
        rule_type=rule_type,
        condition=condition,
        output=output
    )
    db.session.add(rule)
    db.session.commit()