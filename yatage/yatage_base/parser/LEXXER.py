from pyparsing import Word, oneOf, MatchFirst, Optional, ZeroOrMore, OneOrMore

caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowers = caps.lower()
digits = "0123456789"
punctuation = "!@#$%^&*(){}"
ignore_words = ['the','it','and',"on",'big','small','a',"of","to","from","out"] #,Literal(punctuation)]


WORD = Word( caps + lowers )
INTEGER = Word( digits )
TAKE = oneOf(["get","take","pick up","grab"],True,False)
DROP = oneOf(["put down","drop"],True,False)
PUT = oneOf(["place","give","put"],True,False)
WEAR = oneOf(["wear","equip","put on"])
USE = oneOf(["use","use"],True,False)
GO = oneOf(["go","move","exit"])
NORTH = oneOf(["n","north","up"],True,False)

SOUTH = oneOf(["s","south","down"],True,False)
EAST = oneOf(["e","east","right"],True,False)
WEST = oneOf(["w","west","left"],True,False)
DIRECTION = MatchFirst([NORTH,SOUTH,EAST,WEST])

OPTIONAL_COUNT = Optional(INTEGER,"all")
TARGET = OneOrMore(WORD)
IGNOREABLES = ZeroOrMore(oneOf(ignore_words))

#// NORMALIZE OUR DIRECTIONS
NORTH.setParseAction(lambda: [{'direction': 'NORTH', 'key': 0}, ])
EAST.setParseAction(lambda: [{'direction': 'EAST', 'key': 1}, ])
SOUTH.setParseAction(lambda: [{'direction': 'SOUTH', 'key': 2}, ])
WEST.setParseAction(lambda: [{'direction': 'WEST', 'key': 3}, ])
TARGET.setParseAction(lambda t: [{'target': [x for x in t]}])
OPTIONAL_COUNT.setParseAction(lambda t: [{'count': t[0]}, ])