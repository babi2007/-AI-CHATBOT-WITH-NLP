import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    [r"what is your name?", ["I'm a simple chatbot."]],
    [r"how are you?", ["I'm good, thanks for asking!", "Doing well."]],
    [r"what can you do?", ["I can answer basic questions."]],
    [r"who created you?", ["I was created as part of an internship project."]],
    [r"bye", ["Goodbye!", "See you later!", "Bye!"]],
]

chatbot = Chat(pairs, reflections)

print("Hi! I'm your chatbot. Type 'bye' to exit.")
chatbot.converse()
