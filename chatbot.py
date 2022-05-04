from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

flexbot = ChatBot(name='Flex Bot', read_only=True,
                  logic_adapters=[
                      {
                          'import_path': 'chatterbot.logic.BestMatch',
                          'default_response': 'I am so sorry. I can\'t help you right now, please contact the nearest therapist to you',
                          'maximum_similarity_threshold': 0.80
                      }
                  ])

trainer = ListTrainer(flexbot)
data = open('data', 'r').read().splitlines()
trainer.train(data)


def chat_response(msg):
    return flexbot.get_response(msg)
