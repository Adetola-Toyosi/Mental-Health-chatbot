from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

mbot = ChatBot(name='mbot', read_only=True,
               logic_adapters=[
                    'chatterbot.logic.BestMatch'])

conversations = [
    'hi',
    'hello',
    'how are you?',
    'how are you doing?',
    'i\'m cool.',
    'fine, you?',
    'glad to hear that.',
    'i\'m sad',
    'Sadness is an emotional pain associated with feelings of disadvantages, loss, despair, grief, hopelessness, disappointment and sorrow.'
    ' Do you want me to sing for you?',
    'yes',
    'Twinkle Twinkle Little Star, how i wonder what you are'
    'i\'m angry',
    'why are you angry?',
    'not so good',
    'sorry to hear that',
    'I\'m sorry i cannot help now, please contact 999 for further help'
]

list_trainer = ListTrainer(mbot)
list_trainer.train(conversations)


def chat_response(msg):
    return mbot.get_response(msg)