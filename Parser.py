import os
import sys

__author__ = 'amircohen'

import re
import pickle
import emoji_parse
import trainer
import numpy

TIMESTAMP_REGEX = "(\d+)\/(\d+)\/(\d+)\D+(\d+):(\d+)"
DB_REGEX = TIMESTAMP_REGEX + "...([^:]+):\s([^:]+)"

MONTH, DAY, YEAR, HRS, MNS, SENDER, MESSAGE = [1, 2, 3, 4, 5, 6, 7]

def parse_emojis(string):
    parsed_message = dict.add_emoji_count(string)
    if parsed_message:
        for pair in parsed_message:
            messages_list.append(parse_income_msg(pair[0]))
            emojis_list.append(pair[1])
    return


def parseConversation(convAddress, user):

    conversations = create_conversations_array(convAddress)

    for conv in conversations:
        address = convAddress + conv
        print (address)
        with open(address, "r", -1, "UTF-8") as file:
            line = file.readline()
            while line != "":
                    match = re.match(DB_REGEX, line)
                    if match is not None:
                        sender = match.group(SENDER)
                        if sender == user:
                            msg = match.group(MESSAGE)
                            parse_emojis(msg)
                    line = file.readline()

def save_to_pickle(path_and_name, var):
    with open(path_and_name,'wb') as new_file:
        pickle.dump(var,new_file)

def parse_income_msg(msg):
    msg_dict = {}
    for word in msg.split(" "):
        if word not in [" ", ""]:
            if word not in msg_dict:
                msg_dict[word] = 1
            else:
                msg_dict[word] += 1
    return msg_dict

def create_conversations_array(dir):
    conv_array = []
    conversations = os.listdir(dir)
    for file in conversations:
        if (file != ".DS_Store"):
            conv_array.append(file)
    return conv_array

def test_result(msg):
    with open("classifier.p", "rb") as newfile:
        classifier = pickle.load(newfile)
    with open("vectorizer.p", "rb") as newfile:
        vec = pickle.load(newfile)
    msg_dict = parse_income_msg(msg)
    msg_vec = vec.transform(msg_dict)
    # result = classifier.predict(msg_vec)
    result = classifier.decision_function(msg_vec)
    # result = contacts[classifier.predict(msg_vec)[0]]
    return result


if __name__ == "__main__":
    messages_list = []
    emojis_list = []

    # create the emoji dictionary:
    dict = emoji_parse.EmojiDict()

    users = os.listdir("./users")
    for user in users:
        if (user != ".DS_Store"):
            conversationsDir = "./users/" + user + "/conversations/"
            parseConversation(conversationsDir, user)

            save_to_pickle("./users/" + user + "/messages.p",
                           messages_list)
            save_to_pickle("./users/" + user + "/emojis.p", emojis_list)

            trainer.train("./users/" + user + "/")
















