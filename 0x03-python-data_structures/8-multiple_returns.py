#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    tuple_a = (length, sentence[:1]) if sentence else (length, None)
    return (tuple_a)
