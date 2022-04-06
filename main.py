import datetime


def greeting():
    hour = int(datetime.datetime.now().hour)
    # print(hour)
    if hour >= 0 and hour < 12:
        return "Good Morning!"
    elif hour >= 12 and hour < 18:
        return "Good Afternoon!"
    else:
        return "Good Evening!"


def welcome():
    return f'{greeting()}, How can I help?'


def further_help():
    return 'I am really sorry that I cannot help you further, please call \'999\' for help'


def greet():
    return 'I\'m fine and you?'


def greet_response():
    return 'That\'s great to hear!'


def sad_response(sad_reply):
    return f'Do you know why you are {sad_reply}? '

def bye():
    return 'Goodbye, Let\'s talk later.'



