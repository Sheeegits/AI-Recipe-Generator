from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Tracker
from typing import Dict, List

# Example recipes
RECIPES = {
    "butter chicken": "To make Butter Chicken: Marinate chicken with yogurt and spices, cook in a creamy tomato sauce, and serve with rice or naan.",
    "pasta": "To make Pasta: Boil pasta, sauté garlic in olive oil, add tomatoes, mix with cooked pasta, and top with cheese.",
    "chicken": "To make a Chicken Dish: Cook chicken with spices, onions, and tomatoes, then serve hot.",
    "fish": "To make a Fish Dish: Grill fish with lemon and herbs, serve with rice or salad.",
    "tomato": "Try making Tomato Soup: Blend cooked tomatoes, add cream and spices, and serve hot.",
    "spinach": "Make Spinach Curry: Cook spinach with onions, garlic, and spices for a healthy dish."
}

class ActionGetRecipe(Action):
    def name(self):
        return "action_get_recipe"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict):
        # Extract ingredient entity
        ingredient = next(tracker.get_latest_entity_values("ingredient"), None)

        if ingredient and ingredient.lower() in RECIPES:
            response = f"Here is a recipe for {ingredient.capitalize()}:\n{RECIPES[ingredient.lower()]}"
        else:
            response = "Sorry, I don't have a recipe for that ingredient. Try another one!"

        dispatcher.utter_message(text=response)
        return []
