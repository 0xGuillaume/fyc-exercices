import random


items = []
os = ["ubuntu", "fedora", "rhel"]

for index in range(0, 2):
    item = {
        "Item": {
            "os": {"S": random.choice(os)},
            "uptodate": {"BOOL": str(random.choice([True, False]))},
            "installed_on": {"N": str(random.randint(1, 500))},
        }
    }
    items.append(item)

print(items)
