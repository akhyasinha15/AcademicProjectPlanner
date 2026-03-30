from data.rules import PLANNING_RULES, ARCH_RULES

def evaluate_rules(data):
    result = {}

    # Planning Rule
    for rule in PLANNING_RULES:
        if rule["condition"](data):
            result["planning"] = rule
            break

    # Default fallback (VERY IMPORTANT)
    if "planning" not in result:
        result["planning"] = PLANNING_RULES[0]

    # Architecture Rule
    for rule in ARCH_RULES:
        if rule["condition"](data):
            result["architecture"] = rule
            break

    # Default fallback
    if "architecture" not in result:
        result["architecture"] = ARCH_RULES[0]

    return result