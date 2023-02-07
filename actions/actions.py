# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import random

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionPlayRPS(Action):

    def name(self) -> Text:
        return "action_play_rps"

    def computer_choice(self):
        generatedNum = random.randint(1,3)
        if generatedNum == 1:
            computerChoice = "rock"
        elif generatedNum == 2:
            computerChoice = "paper"
        elif generatedNum == 3:
            computerChoice = "scissors"
        
        return (computerChoice)
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text,Any]) -> List[Dict[Text,Any]]:
        
        # Play Rock Paper Scissors
        
        user_choice = tracker.get_slot("choice")
        dispatcher.utter_message(text=f"You Chose {user_choice}")
        comp_choice = self.computer_choice()
        dispatcher.utter_message(text=f"The Computer Chose {comp_choice}")
        
       
        if user_choice == "rock" and comp_choice == "scissors":
            dispatcher.utter_message(text="Congrats, You Won!")
        elif user_choice == "rock" and comp_choice == "paper":
            dispatcher.utter_message(text="The Computer Won!")
        elif user_choice == "paper" and comp_choice == "rock":
            dispatcher.utter_message(text="Congrats, You Won!")
        elif user_choice == "paper" and comp_choice == "scissors":
            dispatcher.utter_message(text="The Computer Won!")
        elif user_choice == "scissors" and comp_choice == "paper":
            dispatcher.utter_message(text="Congrats, You Won!")
        elif user_choice == "scissors" and comp_choice == "rock":
            dispatcher.utter_message(text="The Computer Won!")
        else:
            dispatcher.utter_message(text="It was a tie")
       
       
        return []
    