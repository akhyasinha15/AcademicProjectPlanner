from flask import Blueprint, render_template, request, redirect, session

from application.validation import validate_input
from application.rule_engine import evaluate_rules
from application.planner import generate_plan
from application.architecture import recommend_architecture
from application.gantt import generate_gantt

main_routes = Blueprint("main", __name__)

# =========================
# GLOBAL STATE (Simple storage)
# =========================
project_data_store = {
    "plan": None,
    "architecture": None,
    "chart": None
}

# =========================
# LOGIN ROUTE
# =========================
@main_routes.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Simple login (for demo)
        if username and password:
            session["user"] = username
            return redirect("/dashboard")

    return render_template("login.html", title="Login")


# =========================
# LOGOUT
# =========================
@main_routes.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")


# =========================
# DASHBOARD
# =========================
@main_routes.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")

    return render_template("dashboard.html", title="Dashboard")


# =========================
# INPUT PAGE (HOME)
# =========================
@main_routes.route("/", methods=["GET", "POST"])
def index():
    if "user" not in session:
        return redirect("/login")

    if request.method == "POST":

        try:
            data = {
                "project_type": request.form.get("project_type"),
                "team_size": int(request.form.get("team_size")),
                "duration": int(request.form.get("duration")),
                "technology": request.form.get("technology")
            }
        except:
            return render_template("index.html", errors=["Invalid input format"])

        # VALIDATION
        valid, errors = validate_input(data)
        if not valid:
            return render_template("index.html", errors=errors)

        # RULE ENGINE
        rules = evaluate_rules(data)

        # GENERATION
        plan = generate_plan(data, rules)
        architecture = recommend_architecture(data, rules)
        chart = generate_gantt(plan)

        # STORE (for multi-page navigation)
        project_data_store["plan"] = plan
        project_data_store["architecture"] = architecture
        project_data_store["chart"] = chart

        return redirect("/plan")

    return render_template("index.html", title="Input")


# =========================
# PAGE 1 – PROJECT PLAN
# =========================
@main_routes.route("/plan")
def plan_page():
    if "user" not in session:
        return redirect("/login")

    plan = project_data_store.get("plan")

    if not plan:
        return redirect("/")

    return render_template("plan.html", plan=plan, title="Project Plan")


# =========================
# PAGE 2 – ARCHITECTURE
# =========================
@main_routes.route("/architecture")
def architecture_page():
    if "user" not in session:
        return redirect("/login")

    architecture = project_data_store.get("architecture")

    if not architecture:
        return redirect("/")

    return render_template(
        "architecture.html",
        architecture=architecture,
        title="Architecture"
    )


# =========================
# PAGE 3 – GANTT + CHART
# =========================
@main_routes.route("/gantt")
def gantt_page():
    if "user" not in session:
        return redirect("/login")

    chart = project_data_store.get("chart")
    plan = project_data_store.get("plan")

    if not chart or not plan:
        return redirect("/")

    return render_template(
        "gantt.html",
        chart=chart,
        plan=plan,
        title="Gantt Chart"
    )

@main_routes.route("/api", methods=["POST"])
def api():
    data = request.json

    rules = evaluate_rules(data)
    plan = generate_plan(data, rules)
    architecture = recommend_architecture(data, rules)

    return {
        "plan": plan,
        "architecture": architecture
    }