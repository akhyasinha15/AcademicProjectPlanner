PLANNING_RULES = [
    {
        "condition": lambda d: d["project_type"] == "mini",
        "phases": {
            "Planning": 0.3,
            "Design": 0.2,
            "Implementation": 0.3,
            "Testing": 0.2
        }
    },
    {
        "condition": lambda d: d["project_type"] == "final",
        "phases": {
            "Planning": 0.2,
            "Design": 0.3,
            "Implementation": 0.3,
            "Testing": 0.2
        }
    }
]

ARCH_RULES = [
    {
        "condition": lambda d: d["team_size"] <= 2,
        "type": "Monolithic",
        "description": "Simple architecture for small teams",
        "components": ["UI", "Logic", "Database"]
    },
    {
        "condition": lambda d: d["team_size"] > 2,
        "type": "Three-Tier",
        "description": "Layered scalable architecture",
        "components": ["Presentation", "Application", "Data"]
    }
]