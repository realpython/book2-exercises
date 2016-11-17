
import requests
import json

def index():
    return dict()

def process(my_list):

    # analyze first item
    binary_first = my_list[1]
    output_first = json.loads(binary_first)
    label_first = output_first["label"]

    # analyze second item
    binary_second = my_list[3]
    output_second = json.loads(binary_second)
    label_second = output_second["label"]

    # logic
    if label_first == "pos":
        if label_second !="pos":
            return my_list[0]
        else:
            if output_first["probability"]["pos"] > output_second["probability"]["pos"]:
                return my_list[0]
            else:
                return my_list[2]
    elif label_first =="neg":
        if label_second !="neg":
            return my_list[2]
        else:
            if output_first["probability"]["neg"] < output_second["probability"]["neg"]:
                return my_list[0]
            else:
                return my_list[2]
    elif label_first == "neutral":
        if label_second =="pos":
            return my_list[2]
        elif label_second == "neg":
            return my_list[0]
        else:
            if output_first["probability"]["pos"] > output_second["probability"]["pos"]:
                return my_list[0]
            else:
                return my_list[2]

def pulse():

    session.m=[]
    url = 'http://text-processing.com/api/sentiment/'

    # first item
    text_first = request.vars.first_item
    text_first = text_first.split('_')
    text_first = ' '.join(text_first)
    session.m.append(text_first)
    data_first = {'text': text_first}
    r_first = requests.post(url, data=data_first)
    session.m.append(r_first.content)

    # second item
    text_second = request.vars.second_item
    text_second = text_second.split('_')
    text_second = ' '.join(text_second)
    session.m.append(text_second)
    data_second = {'text': text_second}
    r_second = requests.post(url, data=data_second)
    session.m.append(r_second.content)

    winner = process(session.m)

    return "The winner is {}!".format(winner)
