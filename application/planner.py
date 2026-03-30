def generate_plan(data, rules):
    if rules is None:
        raise Exception("Rules not generated")

    plan_rule = rules.get("planning")

    if plan_rule is None:
        raise Exception("Planning rule missing")

    duration = data["duration"]

    plan = {}
    for phase, percent in plan_rule["phases"].items():
        plan[phase] = round(duration * percent)

    return plan