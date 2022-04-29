from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

flexbot = ChatBot(name='Flex Bot', read_only=True,
               logic_adapters=[
                   'chatterbot.logic.BestMatch',
                   'chatterbot.logic.MathematicalEvaluation',
               ])

trainer = ListTrainer(flexbot)
data = open('data').read().splitlines()
trainer.train(data)


def chat_response(msg):
    return flexbot.get_response(msg)

