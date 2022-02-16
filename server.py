from operator import lt
import random
import string
from flask import Flask, request, Response

server = Flask(__name__)
bag = {}
list_of_words= []
round = 0
first_letter = ""
def data_to_list():
    a_file = open("mot.txt", "r")
    for line in a_file:
        word =line.rstrip()
        list_of_words.append(word)
    a_file.close()

@server.route('/')
def home():
    global bag

    return "\n".join([f"{k}\t{bag[k]}" for k in bag.keys()])


@server.route('/<key>', methods=['GET'])
def get_data(key):
    global bag

    return bag[key] if key in bag else f'Not found', 404


@server.route('/first_letter', methods=['GET'])
def get_letter():
    return f"La lettre est {first_letter}"

@server.route('/<key>', methods=['POST'])
def set_data(key):
    global bag, first_letter
    mot = request.get_data(False, True)
    
    if not mot[0] == first_letter:
        return "Veuillez rentrer un autre mot (la première lettre ne correspond pas)"
    
    if mot in list_of_words:
        first_letter = random.choice(string.ascii_letters).lower()

        return f"Le mot {mot} est accepté"
    else:
        return "Veuillez rentrer un autre mot (le mot n'existe pas)"
    
if __name__ == '__main__':
    first_letter = random.choice(string.ascii_letters).lower()
    data_to_list()
    server.run()
    
