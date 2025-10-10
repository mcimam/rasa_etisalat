# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Dict, List, Text

from rasa_sdk import Action, FormValidationAction, Tracker
from rasa_sdk.events import ActionExecuted, ConversationPaused, UserUtteranceReverted, SlotSet, FollowupAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

TOKEN_OPERATOR = "#ask_operator"
TOKEN_TICKET = "#ticket"
TOKEN_PIN = "#pin"

class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="I'm sorry, I didn't understand that.")
        active_form = tracker.active_loop.get("name")
        print(f"Active form: {active_form}")
        if not active_form:
            dispatcher.utter_message(text="Would you like to speak to a human operator? (yes/no)")

        return []

class ActionConfirmOperator(Action):
    def name(self) -> Text:
        return "action_confirm_operator"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        last_intent = tracker.get_intent_of_latest_message()

        if last_intent in ("affirm", "thank"):
            dispatcher.utter_message(text="Okay, connecting you to a human operator.")
            return [SlotSet("issue_category", "other"), FollowupAction("action_call_operator")]
        elif last_intent == "deny":
            dispatcher.utter_message(text="Okay, let me know if you need help with anything else.")
            return []
        else:
            dispatcher.utter_message(text="Sorry, I didn't get that. Do you want to talk to a human? (yes/no)")
            return []

class ActionCallOperator(Action):
    def name(self) -> Text:
        return "action_call_operator"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        customer_email = tracker.get_slot("customer_email")

        dispatcher.utter_message(text="Connecting to Operator....")
        dispatcher.utter_message(json_message={"token": TOKEN_OPERATOR, "category": tracker.get_slot('issue_category'), "email": customer_email})
        return [ConversationPaused()]


class ActionSubmitTicket(Action):
    def name(self) -> Text:
        return "action_submit_ticket"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Here you can add your logic to submit the ticket
        # For example, you might want to send the ticket data to an external system

        customer_email = tracker.get_slot("customer_email")

        dispatcher.utter_message(text="Your ticket has been submitted successfully!")
        dispatcher.utter_message(json_message={"token": TOKEN_TICKET, "email": customer_email})
        return [SlotSet(key="customer_issue", value=None)]


class ActionPin(Action):
    def name(self) -> Text:
        return "action_pin"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Verifying your PIN, please wait...")
        dispatcher.utter_message(json_message={"token": TOKEN_PIN})
        return [ConversationPaused()]
