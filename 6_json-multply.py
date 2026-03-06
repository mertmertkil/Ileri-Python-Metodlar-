# çoklu liste grupları

db = {
    "users": {
        "mertmertkil": {"firsname": "mert", "lastname": "mertkil"},
        "mervemertkil": {"firstname": "merve", "lastname": "mertkil"},
    },
    "2": {"title": "MacbookAir", "price": 80000},
    "3": {"title": "Samsung S24", "price": 50000},
}

import json

with open("db.json","w") as file:
    json.dump(db, file, indent=2)
