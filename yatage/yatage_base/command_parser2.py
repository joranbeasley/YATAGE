"""Calculate the molecular weight given a molecular formula

Parse the formula using PyParsing.
"""
# pyparsing_mw.py
#
# This code is a modification of
#   http://pyparsing.wikispaces.com/space/showimage/chemicalFormulas.py
# done by Andrew Dalke

# chemicalFormulas.py
#
# Copyright (c) 2003, 2007, Paul McGuire
#
from pip._vendor.distlib.util import OR
from pyparsing import Word, Optional, ZeroOrMore, Group, ParseException, oneOf, Suppress, restOfLine, Literal, Or, \
    OneOrMore, MatchFirst



# define some strings to use later, when describing valid lists
# of characters for chemical symbols and numbers
from yatage.yatage_base.parser.LEXXER import IGNOREABLES, TARGET, GO

caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowers = caps.lower()
digits = "0123456789"
punctuation = "!@#$%^&*(){}"
ignore_words = ['the','it','and',"on",'big','small','a',"of","to","from","out"] #,Literal(punctuation)]
# Define grammar for a chemical formula
# - an element is a Word, beginning with one of the characters in caps,
#   followed by zero or more characters in lowers





def target_action(tokens):
    print("TARGET:",tokens)
    return [{'target':[x for x in tokens]},]



look_command = Group(Literal('look')+Optional(Suppress(oneOf('at towards to',1,0)))+Suppress(IGNOREABLES)+Optional(TARGET,{'target':'CURRENT_ROOM'}))
move_command = Or([Group(GO + Suppress(IGNOREABLES) + DIRECTION),DIRECTION])("GO")
take_command = Group(TAKE + Suppress(IGNOREABLES) + OPTIONAL_COUNT + TARGET("TAKE_TARGET") )("TAKE")
wear_command = Group(WEAR + Suppress(IGNOREABLES) + TARGET("WEAR_TARGET"))
# - an elementRef is an element, optionally followed by an integer - if
#   the integer is omitted, assume the value "1" as a default; these are
#   enclosed in a Group to make it easier to walk the list of parsed
#   chemical symbols, each with its associated number of atoms per
#   molecule





## Add some actions

# Auto-convert integers
def convertIntegers(tokens):
    return int(tokens[0])

# Compute partial molecular weight per element
def computeElementWeight(tokens):
    element = tokens[0]
    element["weight"] = atomicWeight[element.symbol] * element.qty

def take_something(tokens):
    d = {'action':'take'}
    d.update(tokens[0][1])
    d.update(tokens[0][2])
    return [d,]
def wear_something(tokens):
    print("WEAR:",tokens)
    d = {'action':'wear'}
    d.update(tokens[0][1])
    print(d)
    # d.update(tokens[0][1])
    # d.update(tokens[0][2])
    # return d
def look_at_something(tokens):
    d = {'action':'look'}
    target = tokens[0][1]
    if target['target'] == "around":
        target['target'] = "CURRENT_ROOM"
    d.update(target)
    return d
def move_somewhere(tokens):
    ele = tokens[0]
    if isinstance(ele,dict):
        ele = [ele,]
    d = {'action':'move'}
    d.update(ele[-1])
    return d


take_command.setParseAction(take_something)
wear_command.setParseAction(wear_something)
look_command.setParseAction(look_at_something)
move_command.setParseAction(move_somewhere)

command = MatchFirst([take_command,wear_command,look_command,move_command])
print(command.parseString("go n"))
print(command.parseString("n"))
# elementRef.setParseAction( computeElementWeight )

print("OK??")