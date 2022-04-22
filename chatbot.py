from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

mbot = ChatBot(name='mbot', read_only=True,
               logic_adapters=[
                   'chatterbot.logic.BestMatch',
                   'chatterbot.logic.MathematicalEvaluation',
                   {
                       'import_path': 'chatterbot.logic.BestMatch',
                       'default': ["I\'m so sorry I cannot help now, please contact 999 for further help"],
                       'maximum_similarity_threshold': 0.90
                   }
               ])

conversations = [
    'hi',
    'hello',
    'what is your name?',
    'I am Flex Bot',
    'how are you?',
    'I\'m okay, You?',
    'I\'m fine',
    'glad to hear that.',
    'i\'m sad',
    'Sadness is an emotional pain associated with feelings of disadvantages, loss, despair, grief, hopelessness, disappointment and sorrow.'
    'Do you want me to sing for you?',
    'yes',
    'Twinkle Twinkle Little Star, how i wonder what you are',
    'i\'m angry',
    'why are you angry?',
    'sorry to hear that',
]

list_trainer = ListTrainer(mbot)
list_trainer.train(conversations)


def chat_response(msg):
    return mbot.get_response(msg)