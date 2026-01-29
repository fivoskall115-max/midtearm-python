import csv
import random

FILENAME = "recipes.csv"

def load_recipes():
    recipes = []

    try:
        file = open(FILENAME, "r", encoding="utf-8-sig")
        reader = csv.DictReader(file)

        for row in reader:
            row["prep_time"] = int(row["prep_time"])
            recipes.append(row)

        file.close()

    except :
        print("File not found. Starting with empty recipe list.")

    return recipes



def save_recipes(recipes):
    file = open(FILENAME, "w", newline="")

    fieldnames = ["id", "name", "cuisine", "difficulty",
                  "prep_time", "ingredients", "category"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for r in recipes:
        writer.writerow(r)

    file.close()


def view_all(recipes):
    print("\n=== ALL RECIPES ===")

    sorted_recipes = sorted(recipes, key=lambda r: r["name"].lower())

    for r in sorted_recipes:
        print(r["id"] + ". " + r["name"])


def add_recipe(recipes):
    print("\n=== ADD RECIPE ===")

    name = input("Name: ")
    cuisine = input("Cuisine: ")
    difficulty = input("Difficulty: ")
    prep_time = int(input("Prep time (minutes): "))
    ingredients = input("Ingredients with commas: ")
    category = input("Category: ")

    new_id = 1
    for r in recipes:
        if int(r["id"]) >= new_id:
            new_id = int(r["id"]) + 1

    recipe = {}
    recipe["id"] = str(new_id)
    recipe["name"] = name
    recipe["cuisine"] = cuisine
    recipe["difficulty"] = difficulty
    recipe["prep_time"] = prep_time
    recipe["ingredients"] = ingredients
    recipe["category"] = category

    recipes.append(recipe)
    print("Recipe added")


def search(recipes):
    print("\n=== SEARCH ===")
    term = input("Enter cuisine, category, or ingredient: ").lower()

    found = False

    for r in recipes:
        if (term in r["ingredients"].lower() or
            term in r["cuisine"].lower() or
            term in r["category"].lower()):
            print(r["id"] + ". " + r["name"])
            found = True

    if not found:
        print("No recipes found.")


def delete_recipe(recipes):
    print("\n=== DELETE RECIPE ===")
    rid = input("Enter recipe ID: ")

    for i in range(len(recipes)):
        if recipes[i]["id"] == rid:
            del recipes[i]
            print("Recipe deleted.")
            return

    print("Recipe not found.")


def statistics(recipes):
    print("\n=== STATISTICS ===")
    print("Total recipes:", len(recipes))

    cuisine_count = {}
    ingredient_count = {}

    for r in recipes:
        cuisine = r["cuisine"]
        if cuisine in cuisine_count:
            cuisine_count[cuisine] += 1
        else:
            cuisine_count[cuisine] = 1

        ingredients = r["ingredients"].split(",")
        for ing in ingredients:
            ing = ing.strip()
            if ing in ingredient_count:
                ingredient_count[ing] += 1
            else:
                ingredient_count[ing] = 1

    print("\nRecipes by cuisine:")
    for c in cuisine_count:
        print(c + ":", cuisine_count[c])

    print("\nRecipes by ingredient:")
    for i in ingredient_count:
        print(i + ":", ingredient_count[i])

def recommend_recipe(recipes):
    print("\n=== RECOMMEND RECIPE ===")

    if len(recipes) == 0:
        print("No recipes available.")
        return

    category = input("Give category: ")
    same_category = []

    for r in recipes:
        if r["category"].strip().lower() == category.strip().lower():
            same_category.append(r)

    if len(same_category) == 0:
        print("No recipes in this category.")
        return

    index = random.randint(0, len(same_category) - 1)
    recipe = same_category[index]

    print("\nRecommended recipe:")
    print("Name:", recipe["name"])
    print("Cuisine:", recipe["cuisine"])
    print("Difficulty:", recipe["difficulty"])
    print("Prep time:", recipe["prep_time"], "minutes")
    print("Ingredients:", recipe["ingredients"])
    print("Category:", recipe["category"])


def main_menu():
    recipes = load_recipes()

    while True:
        print("""
====== RECIPES MENU ======
1. Add recipe
2. View all recipes
3. Search
4. Delete recipe
5. Statistics
6. Recommend recipe
0. Save and exit
==========================
""")

        choice = input("Choose: ")

        if choice == "1":
            add_recipe(recipes)
        elif choice == "2":
            view_all(recipes)
        elif choice == "3":
            search(recipes)
        elif choice == "4":
            delete_recipe(recipes)
        elif choice == "5":
            statistics(recipes)
        elif choice == "6":
            recommend_recipe(recipes)
        elif choice == "0":
            save_recipes(recipes)
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid choice.")


main_menu()

