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

class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="I am passing you to a human...")
        return [ConversationPaused(), UserUtteranceReverted()]

        # fallback_stage = tracker.get_slot("fallback_stage") or "none"

        # if fallback_stage == "none":
        #     dispatcher.utter_message(text="Sorry, I didn't quite get that. Could you please rephrase?")
        #     return [UserUtteranceReverted(), SlotSet("fallback_stage", "asked_rephrase")]

        # elif fallback_stage == "asked_rephrase":
        #     dispatcher.utter_message(text="Still not sure I understand. Would you like to talk to a human?")
        #     return [SlotSet("fallback_stage", "asked_handoff")]

        # else:
        #     return []
