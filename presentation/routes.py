from flask import Blueprint, render_template, request
from application.validation import validate_input
from application.planner import generate_plan
from application.architecture import recommend_architecture
from application.gantt import generate_gantt
from application.rule_engine import evaluate_rules

main_routes = Blueprint("main", __name__)

@main_routes.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":

        data = {
            "project_type": request.form["project_type"],
            "team_size": int(request.form["team_size"]),
            "duration": int(request.form["duration"]),
            "technology": request.form["technology"]
        }

        valid, errors = validate_input(data)
        if not valid:
            return render_template("index.html", errors=errors)

        rules = evaluate_rules(data)
        plan = generate_plan(data, rules)
        architecture = recommend_architecture(data, rules)

        chart = generate_gantt(plan)

        return render_template(
            "result.html",
            plan=plan,
            architecture=architecture,
            chart=chart
        )
        print("DATA:", data)
        print("RULES:", rules)



    return render_template("index.html")