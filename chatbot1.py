import re
import main as m


def chatbot(user_words):

    hi = ['hi', 'hello', 'hiya', 'hey']
    bye = ['bye', 'goodbye', "bye bye", 'byebye', 'going']
    greet = ['how']
    greet_response = ['okay', 'fine', 'great', 'good']
    sad_reply = ['sad', 'depressed', 'unhappy', 'down', 'angry', 'annoyed']

    key_words = hi, bye, greet, greet_response, sad_reply

    split_input = re.split(r'\s+|[,;?!.-]\s*', user_words.lower())

    try:
        for word in split_input:
            if word in hi:
                return m.welcome()
            elif word in bye:
                return m.bye()
            elif word in greet:
                return m.greet()
            elif word in greet_response:
                return m.greet_response()
            elif word in sad_reply:
                return m.sad_response(word)
            elif word not in key_words:
                def again():
                    for i in split_input:
                        if i not in split_input:
                            return chatbot(split_input)
                    return m.further_help()

    except None:
        return m.further_help()
