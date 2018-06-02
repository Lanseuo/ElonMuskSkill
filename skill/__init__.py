from __future__ import print_function

import skill.intents as intents


def on_session_started(session_started_request, session):
    print("on_session_started")
    pass


def on_session_ended(session_ended_request, session):
    print("on_session_ended")
    pass


def on_intent(intent_request, session):
    intent = intent_request["intent"]["name"]

    if intent == "QuoteIntent":
        return intents.quote_intent()
    elif intent == "WhoIntent":
        return intents.who_intent()
    elif intent == "BirthIntent":
        return intents.birth_intent()
    elif intent == "BirthdayIntent":
        return intents.birthday_intent()
    elif intent == "AgeIntent":
        return intents.age_intent()
    elif intent == "AMAZON.HelpIntent":
        return intents.help_intent()
    elif intent == "AMAZON.StopIntent":
        return intents.stop_intent()
    else:
        raise ValueError(f"Invalid intent {intent}")


def lambda_handler(event, context):

    print("Incoming request ...")

    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event["session"]["new"]:
        on_session_started(
            {"requestId": event["request"]["requestId"]},
            event["session"]
        )

    if event["request"]["type"] == "LaunchRequest":
        return intents.launch()
    elif event["request"]["type"] == "IntentRequest":
        return on_intent(event["request"], event["session"])
    elif event["request"]["type"] == "SessionEndedRequest":
        return on_session_ended(
            {"requestId": event["request"]["requestId"]},
            event["session"]
        )
