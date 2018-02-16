import datetime
import random

from flask import Flask
from flask_ask import Ask, statement

app = Flask(__name__)
ask = Ask(app, "/")


quotes = [
    {
        "headline": "Elon Musk über schlechte Chancen",
        "content": "Wenn etwas wichtig genug ist, dann mach es, auch wenn alle Chancen gegen dich stehen."
    },
    {
        "headline": "Elon Musk über den Aufbau einer Firma",
        "content": "Eine Firma aufzubauen ist wie Kuchen backen. Man braucht von allen Zutaten genau die richtige Menge."
    },
    {
        "headline": "Elon Musk über Geduld",
        "content": "Geduld ist eine Tugend und ich erlerne sie gerade. Es ist eine harte Lehre."
    },
    {
        "headline": "Elon Musk über Ziele",
        "content": "Menschen arbeiten besser, wenn sie wissen für welches Ziel und warum. Es ist wichtig, dass die Leute sich darauf freuen, morgens in die Arbeit zu kommen, und ihnen das Arbeiten Spaß macht."
    },
    {
        "headline": "Elon Musk über großartige Unternehmen",
        "content": "Großartige Unternehmen sind auf großartigen Produkten aufgebaut."
    },
    {
        "headline": "Elon Musk über Innovation",
        "content": "Wie entsteht innovatives Denken? Es ist eine Geisteshaltung, für die man sich entscheiden muss."
    },
    {
        "headline": "Elon Musk über komplizierte Aufgaben",
        "content": "Es ist ein Fehler, eine große Anzahl an Leuten einzustellen, um eine komplizierte Aufgabe zu lösen. Viele können niemals Talent wettmachen, wenn es darum geht, die richtige Lösung zu finden (zwei Menschen, die etwas nicht wissen, sind nicht besser als einer). Sie werden den Fortschritt aufhalten und unglaublich teuer machen."
    },
    {
        "headline": "Elon Musk über Unternehmertum",
        "content": "Unternehmer zu sein ist wie Glas zu essen und in den Abgrund des Todes zu starren."
    },
    {
        "headline": "Elon Musk über Selbstzufriedenheit",
        "content": "Denk immer darüber nach, wie du Dinge besser machen kannst, und hinterfrage dich."
    },
    {
        "headline": "Elon Musk über seinen größten Fehler",
        "content": "Mein größter Fehler ist vermutlich, zu viel Wert auf das Talent von jemanden zu legen und nicht auf seine Persönlichkeit. Ich denke es ist wichtig, dass jemand ein gutes Herz hat."
    },
    {
        "headline": "Elon Musk über die Vergangenheit",
        "content": "Wenn irgendwer lieber in der Vergangenheit leben will, dann kennt er sich mit Geschichte nicht besonders gut aus. Das Leben in früheren Zeiten war zum Kotzen. Die Menschen wussten sehr wenig und man wäre wahrscheinlich in einem jungen Alter an einer furchtbaren Krankheit gestorben. Man hätte jetzt wahrscheinlich keine Zähne mehr. Als Frau wäre es besonders schlimm."
    },
    {
        "headline": "Elon Musk über die Zukunft",
        "content": "Wenn du morgens aufwachst und denkst, dass die Zukunft besser sein wird, ist das ein schöner Tag. Ansonsten ist er es nicht."
    }
]


@ask.intent("QuoteIntent")
def quote_intent():
    quote = random.choice(quotes)
    return statement(quote["content"])\
        .simple_card(quote["headline"], "\"" + quote["content"] + "\"")


@ask.intent("WhoIntent")
def who_intent():
    text = "Elon Reeve Musk ist ein Unternehmer und Investor. Er hat sowohl die Staatsangehörigkeit seines Geburtslandes Südafrika als auch die von Kanada und den Vereinigten Staaten. Musk ist bekannt geworden durch seine Beteiligung an der Gründung des Online-Bezahlsystems PayPal sowie mit seinen Erfolgen mit dem privaten Raumfahrtunternehmen SpaceX und dem Elektroautohersteller Tesla."
    return statement(text)\
        .simple_card("Wer ist Elon Musk?", text)


@ask.intent("BirthIntent")
def birth_intent():
    return statement("Elon Musk wurde am 28. Juni 1971 in Pretoria geboren.")\
        .simple_card("Elon Musks Geburt", "28. Juni 1971 in Pretoria")


@ask.intent("BirthdayIntent")
def birthday_intent():
    day, month = 28, 6
    if (datetime.date(datetime.date.today().year, month, day) - datetime.date.today()).days >= 0:
        # Has not yet have birthday this year
        days_until_birthday = (datetime.date(datetime.date.today().year,
                                             month, day) - datetime.date.today()).days
    else:
        days_until_birthday = (datetime.date(datetime.date.today().year +
                                             1, month, day) - datetime.date.today()).days

    if days_until_birthday == 0:
        text = "Elon Musk hat heute Geburtstag! Alles Gute Elon Musk"
    elif days_until_birthday == 1:
        text = "Elon Musk hat morgen Geburtstag."
    elif days_until_birthday == 2:
        text = "Elon Musk hat übermorgen Geburtstag."
    elif datetime.date(datetime.date.today().year, month, day) - datetime.date.today() == -1:
        text = "Elon Musk hatte gestern Geburtstag."
    elif datetime.date(datetime.date.today().year, month, day) - datetime.date.today() == -2:
        text = "Elon Musk hatte vorgestern Geburstag."
    else:
        text = "Elon Musk hat am 28. Juni Geburtstag. Du musst noch {} Tage bis zu seinem Geburtstag warten.".format(
            days_until_birthday)

    return statement(text)


@ask.intent("AgeIntent")
def age_intent():
    age = datetime.date.today().year - 1971 - ((datetime.date.today().month,
                                                datetime.date.today().day) < (6, 28))
    return statement("Elon Musk ist {} Jahre alt.".format(age))


if __name__ == "__main__":
    app.run(debug=True)
