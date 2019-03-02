import speech_recognition as sr
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def get_user_input():
    r = sr.Recognizer()

    # obtain audio from the microphone
    with sr.Microphone() as source:
        print("Say Something!")
        audio = r.listen(source)

    # recognise speech using Sphinx
    try:
        print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        print("Sphinx couldn't understand the audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))


def tk_clean_string(tk_string):
    # tokenize string
    tk_list = word_tokenize(tk_string)

    # remove stop words
    for x, word in enumerate(tk_list):
        if word in set(stopwords.words('english')):
            del tk_list[x]

    # turn entire list to lower
    tk_list = [x.lower() for x in tk_list]

    return tk_list


if __name__ == '__main__':
    print("-------------------- Let's go --------------------")

    rawString = 'what\'s the weather to be like tomorrow'

    tkString = tk_clean_string(rawString)

    print(tkString)
