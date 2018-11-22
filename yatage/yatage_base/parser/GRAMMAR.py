from pyparsing import Group, Optional, Suppress, oneOf, Literal as L, Or

from yatage.yatage_base.parser.LEXXER import IGNOREABLES, TARGET, GO, DIRECTION, TAKE, OPTIONAL_COUNT, WEAR

LOOK_MODIFIERS = Optional(Suppress(oneOf('at towards to', 1, 0))) + Suppress(IGNOREABLES)

look_command = Group(L('look') + LOOK_MODIFIERS + Optional(TARGET, {'target': 'CURRENT_ROOM'}))
move_command = Or([Group(GO + Suppress(IGNOREABLES) + DIRECTION), DIRECTION])
take_command = Group(TAKE + Suppress(IGNOREABLES) + OPTIONAL_COUNT + TARGET)
wear_command = Group(WEAR + Suppress(IGNOREABLES) + TARGET)


def take_something(tokens):
    d = {'action':'take'}
    d.update(tokens[0][1])
    d.update(tokens[0][2])
    return [d,]
def wear_something(tokens):
    d = {'action':'wear'}
    d.update(tokens[0][1])
    return [d,]
    # d.update(tokens[0][1])
    # d.update(tokens[0][2])
    # return d
def look_at_something(tokens):
    d = {'action':'look'}
    target = tokens[0][1]
    if target['target'] == "around":
        target['target'] = "CURRENT_ROOM"
    d.update(target)
    return [d,]
def move_somewhere(tokens):
    ele = tokens[0]
    if isinstance(ele,dict):
        ele = [ele,]
    d = {'action':'move'}
    d.update(ele[-1])
    return [d,]