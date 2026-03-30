def validate_input(data):
    errors = []

    if not data["project_type"]:
        errors.append("Project type required")

    if data["team_size"] <= 0:
        errors.append("Team size must be greater than 0")

    if data["duration"] <= 0:
        errors.append("Duration must be greater than 0")

    if not data["technology"]:
        errors.append("Technology required")

    return (len(errors) == 0, errors)