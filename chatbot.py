from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

mbot = ChatBot(name='Flex Bot', read_only=True,
               logic_adapters=[
                   'chatterbot.logic.BestMatch',
                   'chatterbot.logic.MathematicalEvaluation',
               ])

trainer = ListTrainer(mbot)
data = open('data').read().splitlines()
trainer.train(data)

def chat_response(msg):
    return mbot.get_response(msg)

