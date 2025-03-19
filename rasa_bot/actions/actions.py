from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Tracker
from typing import Dict, List
import random

# Action to get a recipe based on an ingredient
class ActionGetRecipe(Action):
    def name(self) -> str:
        return "action_get_recipe"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict) -> List[Dict]:
        
        # Get the ingredient slot value
        ingredient = tracker.get_slot("ingredient")
        
        # Check if the ingredient is specified
        if not ingredient:
            dispatcher.utter_message(text="I couldn't detect an ingredient. Can you please specify one?")
            return []
        
        # Simulate getting a recipe based on the ingredient
        recipes = {
            "chicken": {"title": "Grilled Chicken", "instructions": "Grill the chicken for 30 minutes."},
            "tomato": {"title": "Tomato Soup", "instructions": "Boil tomatoes and blend them."},
            "pasta": {"title": "Pasta", "instructions": "Boil pasta and mix with sauce."}
        }
        
        # Get the recipe if available for the ingredient
        recipe = recipes.get(ingredient.lower())
        
        # If recipe found, return the recipe, else inform the user
        if recipe:
            dispatcher.utter_message(text=f"Here is a recipe for {recipe['title']}:\n{recipe['instructions']}")
        else:
            dispatcher.utter_message(text="Sorry, I don't have a recipe for that ingredient.")
        
        return []

# Action to suggest a recipe based on the ingredient slot
class ActionRecipeSuggestion(Action):
    def name(self) -> str:
        return "action_recipe_suggestion"

    def run(self, dispatcher, tracker, domain):
        # Get the ingredient slot value
        ingredient = tracker.get_slot('ingredient')
        
        # Check if the ingredient slot has a value
        if not ingredient:
            dispatcher.utter_message(text="I couldn't detect an ingredient. Could you please provide one?")
            return []
        
        # Recipe suggestion logic
        recipe = f"Here is a recipe suggestion using {ingredient}!"
        
        dispatcher.utter_message(text=recipe)
        
        return []
