from pyparsing import Word, oneOf, MatchFirst, Optional, ZeroOrMore, OneOrMore, Literal, Keyword

caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowers = caps.lower()
digits = "0123456789"
punctuation = "!@#$%^&*(){}"
ignore_words = [Keyword(x) for x in ['the','it','and',"on",'big','small','a',"to","from","out"]] #,Literal(punctuation)]


WORD = Word( caps + lowers )
INTEGER = Word( digits )
TAKE = MatchFirst([Keyword(w) for w in ["get","take","pick up","grab"]])
DROP = MatchFirst([Keyword(w) for w in ["put down","drop"]])
PUT = MatchFirst([Keyword(w) for w in ["place","give","put","hand","offer"]])
WEAR = MatchFirst([Keyword(w) for w in ["wear","equip","put on"]])
USE = MatchFirst([Keyword(w) for w in ["use","use"]])
GO = MatchFirst([Keyword("go"),Keyword("move"),Keyword("exit"),Keyword("navigate")])

ACTIVATE = MatchFirst([Keyword(w) for w in ['activate','turn on','touch']])
DEACTIVATE = MatchFirst([Keyword(w) for w in ['deactivate','turn off','touch']])

NORTH = MatchFirst([Keyword("n"),Keyword("north"),Keyword("up")])
SOUTH = MatchFirst([Keyword(w) for w in ["s","south","down"]])
EAST = MatchFirst([Keyword(w) for w in ["e","east","right"]])
WEST = MatchFirst([Keyword(w) for w in ["w","west","left"]])
DIRECTION = MatchFirst([NORTH,SOUTH,EAST,WEST,WORD])

COUNT = MatchFirst(INTEGER,Literal("all"))
TARGET = OneOrMore(WORD,stopOn=MatchFirst(ignore_words))
IGNOREABLES = ZeroOrMore(MatchFirst(ignore_words))

# // BATTLE VERBS
RUN_AWAY = oneOf(['run','run away','flee'],True,False)
ENGAGE = oneOf(['attack','pounce','fight','engage'],True,False)
BLOCK = oneOf(['dodge','parry','block'],True,False)



def set_target(t):
   r = [{'target': [x for x in t]}]
   print(r)
   return r
#// NORMALIZE OUR DIRECTIONS
NORTH.setParseAction(lambda: [{'direction': 'NORTH', 'key': 0}, ])
EAST.setParseAction(lambda: [{'direction': 'EAST', 'key': 1}, ])
SOUTH.setParseAction(lambda: [{'direction': 'SOUTH', 'key': 2}, ])
WEST.setParseAction(lambda: [{'direction': 'WEST', 'key': 3}, ])
TARGET.setParseAction(set_target )
COUNT.setParseAction(lambda t: [{'count': t[0]}, ])