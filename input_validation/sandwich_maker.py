import pyinputplus as pyip

prices = {
    'bread': {
        'wheat': 1.00,
        'white': 1.00,
        'sourdough': 1.25
    },
    'protein': {
        'chicken': 2.50,
        'turkey': 2.75,
        'ham': 2.25,
        'tofu': 2.00
    },
    'cheese': {
        'cheddar': 0.50,
        'Swiss': 0.75,
        'mozzarella': 0.65
    },
    'extras': {
        'mayo': 0.25,
        'mustard': 0.25,
        'lettuce': 0.30,
        'tomato': 0.30
    }
}

print("Welcome to the Sandwich Maker!")

bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt="Choose a bread type:\n", numbered=True)

protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt="Choose a protein:\n", numbered=True)


wants_cheese = pyip.inputYesNo("Do you want cheese? (yes/no): ")
cheese = None
if wants_cheese == 'yes':
    cheese = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], prompt="Choose a cheese type:\n", numbered=True)


extras_selected = []
for extra in ['mayo', 'mustard', 'lettuce', 'tomato']:
    wants_extra = pyip.inputYesNo(f"Do you want {extra}? (yes/no): ")
    if wants_extra == 'yes':
        extras_selected.append(extra)


num_sandwiches = pyip.inputInt("How many sandwiches would you like? (must be 1 or more): ", min=1)

total_cost = 0
total_cost += prices['bread'][bread]
total_cost += prices['protein'][protein]
if cheese:
    total_cost += prices['cheese'][cheese]
for extra in extras_selected:
    total_cost += prices['extras'][extra]

total_cost *= num_sandwiches

print(f"\nThank you! You ordered {num_sandwiches} sandwich(es).")
print(f"Total cost: ${total_cost:.2f}")
