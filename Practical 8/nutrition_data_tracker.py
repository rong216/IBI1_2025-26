# Practical 8 - nutrition_data_tracker.py
# Pseudocode:
# 1. Define a class called food_item
# 2. Store the nutritional values for each food
# 3. Define a function that takes a list of consumed food items
# 4. Calculate the total calories, protein, carbohydrates, and fat
# 5. Print the totals
# 6. Print warnings if calories are above 2500 or fat is above 90 g
# 7. Include an example of using the class and function

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

    print("Daily totals:")
    print(f"Calories: {total_calories}")
    print(f"Protein: {total_protein} g")
    print(f"Carbohydrates: {total_carbohydrates} g")
    print(f"Fat: {total_fat} g")

    if total_calories > 2500:
        print("Warning: calorie intake is above 2,500 calories.")
    if total_fat > 90:
        print("Warning: fat intake is above 90 g.")

    return {
        "calories": total_calories,
        "protein": total_protein,
        "carbohydrates": total_carbohydrates,
        "fat": total_fat
    }


if __name__ == "__main__":
    # Example food items (per serving)
    apple = food_item("Apple", 60, 0.3, 15, 0.5)
    oatmeal = food_item("Oatmeal", 250, 8, 45, 5)
    chicken_sandwich = food_item("Chicken sandwich", 650, 35, 50, 25)
    pasta = food_item("Pasta", 700, 20, 100, 18)
    ice_cream = food_item("Ice cream", 320, 5, 35, 16)

    # Example list of foods consumed over 24 hours
    consumed_today = [
        apple,
        oatmeal,
        chicken_sandwich,
        pasta,
        ice_cream,
        ice_cream,
        pasta
    ]

    calculate_daily_totals(consumed_today)