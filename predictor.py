import os
import pickle
import numpy
from Parser import parse_income_msg


def test_result(address, msg):
    with open(address + "classifier.p", "rb") as newfile:
        classifier = pickle.load(newfile)
    with open(address + "vectorizer.p", "rb") as newfile:
        vec = pickle.load(newfile)
    msg_dict = parse_income_msg(msg)
    msg_vec = vec.transform(msg_dict)
    # result = classifier.predict(msg_vec)
    result = classifier.decision_function(msg_vec)
    # result = contacts[classifier.predict(msg_vec)[0]]
    return result


def find_emojis(string):
    address = "./static/users/kaplan daphna/"
    with open(address + "classes.p", "rb") as classes_file:
        classes = pickle.load(classes_file)
    # print ("The message:")
    # print (string)
    result = (test_result(address, string))
    arr = numpy.array(abs(result[0]))
    sortedArr = arr.argsort()
    indices = (sortedArr[:3][::1])
    # print (classes[indices[0]], arr[sortedArr[0]])
    # print (classes[indices[1]], arr[sortedArr[1]])
    # print (classes[indices[2]], arr[sortedArr[2]])
    # print ("-------------------------------")
    return classes[indices[0]], classes[indices[1]], classes[indices[2]]