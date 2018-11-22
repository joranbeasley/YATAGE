from pyparsing import Group, Optional, Suppress, oneOf, Literal as L, Or, MatchFirst, Literal

from yatage.yatage_base.parser.LEXXER import IGNOREABLES, TARGET, GO, DIRECTION, TAKE, COUNT, WEAR, DROP, PUT, USE

LOOK_MODIFIERS = Optional(Suppress(oneOf('at towards to', 1, 0))) + Suppress(IGNOREABLES)

look_command = Group(oneOf('look') + LOOK_MODIFIERS + Optional(TARGET, {'target': 'CURRENT_ROOM'}))
move_command = Or([Group(GO + Suppress(IGNOREABLES) + DIRECTION), DIRECTION])
take_command = Group(TAKE + Suppress(IGNOREABLES) + Optional(COUNT,{'count':'all'}) + TARGET)
drop_command = Group(DROP + Suppress(IGNOREABLES) + Optional(COUNT,{'count':1}) + TARGET)
wear_command = Group(WEAR + Suppress(IGNOREABLES) + TARGET)
use_command = Group(USE + Suppress(IGNOREABLES) + TARGET + Suppress(Optional(Literal('on'))) + Suppress(IGNOREABLES) + Optional(TARGET,{'target':'CURRENT_PLAYER'}))
put_command = Group(PUT + Suppress(IGNOREABLES) + TARGET + Suppress(IGNOREABLES)+TARGET)
def drop_something(tokens):
    d = {'action': 'drop'}
    d.update(tokens[0][1])
    d.update(tokens[0][2])
    return [d, ]

drop_command.setParseAction(drop_something)
def take_something(tokens):
    d = {'action':'take'}
    d.update(tokens[0][1])
    d.update(tokens[0][2])
    return [d,]
take_command.setParseAction(take_something)
def put_something(tokens):
    print("PUT COMMAND",tokens)
    r = {'action':'give','what':tokens[0][1]['target'],'target':tokens[0][2]['target']}
    return [r,]
put_command.setParseAction(put_something)

def wear_something(tokens):
    d = {'action':'wear'}
    d.update(tokens[0][1])
    return [d,]


wear_command.setParseAction(wear_something)

def look_at_something(tokens):
    d = {'action':'look'}
    target = tokens[0][1]
    if target['target'] == ["around"]:
        target['target'] = "CURRENT_ROOM"
    d.update(target)
    return [d,]

look_command.setParseAction(look_at_something)

def move_somewhere(tokens):
    ele = tokens[0]
    if isinstance(ele,dict):
        ele = [ele,]
    d = {'action':'move'}
    d.update(ele[-1])
    return [d,]

move_command.setParseAction(move_somewhere)
normal_statement = MatchFirst([look_command,wear_command,take_command,drop_command,put_command,move_command])

