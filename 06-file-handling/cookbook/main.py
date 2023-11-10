from pathlib import Path
from os import system
import shutil

def confirm_user_input(message: str) -> bool:
    while True:
        user_input = input(f"{message} (Y/n): >").lower()
        if user_input == "" or user_input == "y":
            return True
        elif user_input == "n":
            return False
        else:
            continue


def get_number_in_range(valid_range: range):
    while True:
        try:
            user_number_input = int(input("Choose one: > "))
            if user_number_input in valid_range:
                return user_number_input
        except ValueError:
            continue


def get_a_category_from_user(cookbook_path: Path) -> Path:
    categories = [child for child in cookbook_path.iterdir() if child.is_dir()]

    print("The available categories are:")
    for (i, category) in enumerate(categories):
        print(f"{i + 1}. {category.stem}")

    selected_number = get_number_in_range(range(1, len(categories) + 1))
    print()

    return categories[selected_number - 1]


def get_a_recipe_from_user(category_path: Path) -> Path:
    recipes = list(category_path.glob("*.txt"))

    print(f"The available recipes in \"{category_path.stem}\" are:")
    for (i, recipe) in enumerate(recipes):
        print(f"{i + 1}. {recipe.stem}")

    selected_number = get_number_in_range(range(1, len(recipes) + 1))
    print()

    return recipes[selected_number - 1]


def welcome(cookbook_path: Path):
    print("Welcome to Juanes's recipe cookbook, here you will find several delicious recipes grouped by categories.")

    print(f"All categories and recipes will be saved in the following path: {cookbook_path}")

    total_recipes = len(list(cookbook_path.glob("*/*.txt")))
    print(f"There are currently {total_recipes} recipes in the book.")


def read_recipe(cookbook_path: Path):
    if len(list(cookbook_path.iterdir())) == 0:
        print(f"The cookbook hasn't categories and recipes yet. You can create the first!")
        print()
        return

    selected_category = get_a_category_from_user(cookbook_path)
    if len(list(selected_category.iterdir())) == 0:
        print(f'The category "{selected_category.stem}" hasn\'t recipes yet. You can create the first!')
        print()
        return

    selected_recipe = get_a_recipe_from_user(selected_category)

    print(f'The content of recipe "{selected_recipe.stem}" is:')

    recipe_file_handler = selected_recipe.open()
    for line in recipe_file_handler:
        print(f"\t{line}")
    recipe_file_handler.close()

    print()


def create_recipe(cookbook_path: Path):
    if len(list(cookbook_path.iterdir())) == 0:
        print(f"The cookbook hasn't categories and recipes yet. You can create the first!")
        print()
        return

    category_path = get_a_category_from_user(cookbook_path)
    new_recipe_name = input("Type a name for the new recipe: > ")
    new_recipe_content = input("Type the content for the new recipe:\n")

    new_recipe_path = category_path / new_recipe_name
    new_recipe_path = new_recipe_path.with_suffix(".txt")

    if new_recipe_path.exists():
        print(f'The recipe "{new_recipe_name}" already exists in the category "{new_recipe_content}"')
        is_user_sure = confirm_user_input("you want to overwrite it?")

        if not is_user_sure:
            print("Creation canceled")
            print()
            return

    new_recipe_path.write_text(new_recipe_content)
    print(f'The recipe "{new_recipe_name}" was successfully created')
    print()


def create_category(cookbook_path: Path):
    new_category_name = input("Type a name for the new category: > ")
    new_category_path = cookbook_path / new_category_name

    if new_category_path.exists():
        print(f'The category {new_category_name} already exists')
    else:
        new_category_path.mkdir()
        print(f'The category {new_category_name} was successfully created')

    print()

def remove_recipe(cookbook_path: Path):
    if len(list(cookbook_path.iterdir())) == 0:
        print(f"The cookbook hasn't categories and recipes yet. You can create the first!")
        print()
        return

    selected_category_path = get_a_category_from_user(cookbook_path)
    if len(list(selected_category_path.iterdir())) == 0:
        print(f'The category "{selected_category_path.stem}" hasn\'t recipes yet. You can create the first!')
        print()
        return

    selected_recipe = get_a_recipe_from_user(selected_category_path)
    selected_recipe.unlink()

    print(f'The recipe "{selected_recipe.stem}" was successfully removed')
    print()


def remove_category(cookbook_path: Path):
    if len(list(cookbook_path.iterdir())) == 0:
        print(f"The cookbook hasn't categories and recipes yet. You can create the first!")
        print()
        return

    selected_category_path = get_a_category_from_user(cookbook_path)
    total_recipes_in_category = len(list(selected_category_path.glob("*.txt")))

    if total_recipes_in_category > 0:
        print(f'The category "{selected_category_path.stem}" has {total_recipes_in_category} recipes')
        print("If you delete it, all the recipes in it will also be deleted")
        is_user_sure = confirm_user_input("Are you sure you want to be remove it?")

        if not is_user_sure:
            print(f'The remove of category "{selected_category_path.stem}" was successfully canceled')
            return

        shutil.rmtree(selected_category_path)
        print(f'The category "{selected_category_path.stem}" and its recipes were successfully removed')
    else:
        if len(list(selected_category_path.iterdir())) > 0:
            shutil.rmtree(selected_category_path)
        else:
            selected_category_path.rmdir()

        print(f'The category "{selected_category_path.stem}" was successfully removed')

    print()


def main():
    cookbook_path = Path.cwd().parent / "Recetas"

    print("======== THE COOKBOOK ========")
    welcome(cookbook_path)
    print()

    while True:
        actions = ["Read recipe", "Create recipe", "Create category", "Remove recipe", "Remove category",
                   "Exit the cookbook"]
        print("MENU OPTIONS")
        for (i, option) in enumerate(actions):
            print(f"{i+1}.", option)
        selected_action = get_number_in_range(range(1, len(actions) + 1))
        print()

        print(actions[selected_action - 1].upper())
        match selected_action:
            case 1:
                read_recipe(cookbook_path)
            case 2:
                create_recipe(cookbook_path)
            case 3:
                create_category(cookbook_path)
            case 4:
                remove_recipe(cookbook_path)
            case 5:
                remove_category(cookbook_path)
            case _:
                break

        input("Press enter key to return to the main menu")
        system('cls')

    print("======== END COOKBOOK ========")


if __name__ == '__main__':
    main()
