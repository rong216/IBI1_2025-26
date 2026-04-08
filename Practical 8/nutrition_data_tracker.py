# Nutrition data tracker

class food_item:
    def __init__(self, name, calories, protein, carbohydrates, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fat = fat


def calculate_daily_totals(consumed_items):
    total_calories = 0
    total_protein = 0
    total_carbohydrates = 0
    total_fat = 0

    for item in consumed_items:
        total_calories += item.calories
        total_protein += item.protein
        total_carbohydrates += item.carbohydrates
        total_fat += item.fat

    print("\nDaily totals:")
    print("Calories:", total_calories)
    print("Protein:", total_protein, "g")
    print("Carbohydrates:", total_carbohydrates, "g")
    print("Fat:", total_fat, "g")

    if total_calories > 2500:
        print("Warning: calorie intake is above 2,500 calories.")
    if total_fat > 90:
        print("Warning: fat intake is above 90 g.")


# food list (per serving)
apple = food_item("Apple", 60, 0.3, 15, 0.5)
oatmeal = food_item("Oatmeal", 250, 8, 45, 5)
chicken_sandwich = food_item("Chicken sandwich", 650, 35, 50, 25)
pasta = food_item("Pasta", 700, 20, 100, 18)
ice_cream = food_item("Ice cream", 320, 5, 35, 16)

foods = [apple, oatmeal, chicken_sandwich, pasta, ice_cream]

consumed_today = []

print("Nutrition Data Tracker")
print("Please enter how many servings you ate for each food.\n")

for food in foods:
    quantity = int(input("How many servings of " + food.name + " did you eat? "))

    if quantity > 0:
        eaten_food = food_item(
            food.name,
            food.calories * quantity,
            food.protein * quantity,
            food.carbohydrates * quantity,
            food.fat * quantity
        )
        consumed_today.append(eaten_food)

calculate_daily_totals(consumed_today)