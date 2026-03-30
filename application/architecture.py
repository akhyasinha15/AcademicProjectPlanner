import os

def recommend_architecture(data, rules):
    rule = rules["architecture"]

    image_map = {
        "Monolithic": "images/monolithic.png",
        "Three-Tier": "images/three_tier.png",
        "Microservices": "images/microservices.png",
        "MVC": "images/mvc.png",
        "Client-Server": "images/client_server.png"
    }

    return {
        "type": rule["type"],
        "description": rule["description"],
        "components": rule["components"],
        "image": image_map.get(rule["type"], "images/default.png")
    }