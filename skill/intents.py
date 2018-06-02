import datetime
import random

from .helpers import answer, question
from .quotes import quotes


def launch():
    return question("Was möchtest Du über Elon Musk wissen?")


def quote_intent():
    quote = random.choice(quotes)
    return answer(quote["content"])


def who_intent():
    return answer(
        "Elon Reeve Musk ist ein Unternehmer und Investor. "
        "Er hat sowohl die Staatsangehörigkeit seines Geburtslandes "
        "Südafrika als auch die von Kanada und den Vereinigten "
        "Staaten. Musk ist bekannt geworden durch seine Beteiligung "
        "an der Gründung des Online-Bezahlsystems PayPal sowie mit "
        "seinen Erfolgen mit dem privaten Raumfahrtunternehmen "
        "SpaceX und dem Elektroautohersteller Tesla.")


def birth_intent():
    return answer("Elon Musk wurde am 28. Juni 1971 in Pretoria geboren.")


def birthday_intent():
    day, month = 28, 6
    today = datetime.date.today()
    if (datetime.date(today.year, month, day) - today).days >= 0:
        # Has not yet have birthday this year
        days_until_birthday = (datetime.date(today.year,
                                             month, day) - today).days
    else:
        days_until_birthday = (datetime.date(today.year +
                                             1, month, day) - today).days

    if days_until_birthday == 0:
        text = "Elon Musk hat heute Geburtstag! Alles Gute Elon Musk!"
    elif days_until_birthday == 1:
        text = "Elon Musk hat morgen Geburtstag."
    elif days_until_birthday == 2:
        text = "Elon Musk hat übermorgen Geburtstag."
    elif datetime.date(today.year, month, day) - today == -1:
        text = "Elon Musk hatte gestern Geburtstag."
    elif datetime.date(today.year, month, day) - today == -2:
        text = "Elon Musk hatte vorgestern Geburstag."
    else:
        text = (
            "Elon Musk hat am 28. Juni Geburtstag. "
            f"Du musst noch {days_until_birthday} Tage bis zu "
            "seinem Geburtstag warten."
        )

    return answer(text)


def age_intent():
    today = datetime.date.today()
    age = today.year - 1971 - ((today.month,
                                today.day) < (6, 28))
    return answer(f"Elon Musk ist {age} Jahre alt.")


def stop_intent():
    pass


def help_intent():
    return answer("Frage Elon Musk zum Beispiel"
                  " .. Alexa, frage Elon Musk, wie alt er ist.")
