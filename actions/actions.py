# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import ConversationPaused, UserUtteranceReverted, SlotSet
from rasa_sdk.executor import CollectingDispatcher

TOKEN_OPERATOR = "#ask_operator"
TOKEN_TICKET = "#ticket"
TOKEN_PIN = "#pin"

class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="I am passing you to a human...")
        dispatcher.utter_message(text=TOKEN_OPERATOR)
        return [ConversationPaused(), UserUtteranceReverted()]

        # fallback_stage = tracker.get_slot("fallback_stage") or "none"

class ActionSubmitTicket(Action):
    def name(self) -> Text:
        return "action_submit_ticket"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Here you can add your logic to submit the ticket
        # For example, you might want to send the ticket data to an external system

        dispatcher.utter_message(text="Your ticket has been submitted successfully!")
        dispatcher.utter_message(text=TOKEN_TICKET)
        return [SlotSet(key="customer_issue", value=None)]


class ActionPin(Action):
    def name(self) -> Text:
        return "action_pin"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Verifying your PIN, please wait...")
        dispatcher.utter_message(text=TOKEN_PIN)
        return [ConversationPaused()]