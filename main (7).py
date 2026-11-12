households = [
    (100, False, False),
    (101, True, False),
    (150, False, False),
    (200, True, False),
    (201, False, False),
    (250, False, True),
    (80, False, False),
    (180, True, True)
]

print("Separate If Statements")

for units, ration_card, senior in households:
    if units <= 100:
        print("Full Subsidy")
    if 101 <= units <= 200 and ration_card:
        print("Partial Subsidy")
    if units > 200 and senior:
        print("Senior Citizen Subsidy")
    if units > 200 and not senior:
        print("No Subsidy")

print("\nIf-Elif-Else")

for units, ration_card, senior in households:
    if units <= 100:
        print("Full Subsidy")
    elif 101 <= units <= 200:
        if ration_card:
            print("Partial Subsidy")
        else:
            print("No Subsidy")
    elif units > 200:
        if senior:
            print("Senior Citizen Subsidy")
        else:
            print("No Subsidy")