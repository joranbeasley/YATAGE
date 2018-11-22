from pyparsing import Group, Literal, Optional, Suppress, oneOf, Or

from yatage.yatage_base.parser.LEXXER import NORTH, EAST, SOUTH, WEST, TARGET, OPTIONAL_COUNT, IGNOREABLES, GO, \
    DIRECTION, TAKE, WEAR


class parser():
    def take_something(self,tokens):
        d = {'action': 'take'}
        d.update(tokens[0][1])
        d.update(tokens[0][2])
        return [d, ]

    def wear_something(self,tokens):
        d = {'action': 'wear'}
        d.update(tokens[0][1])
        return d

    def look_at_something(self,tokens):
        d = {'action': 'look'}
        target = tokens[0][1]
        if target['target'] == "around": target['target'] = "CURRENT_ROOM"
        d.update(target)
        return d

    def move_somewhere(self,tokens):
        ele = tokens[0]
        if isinstance(ele, dict):
            ele = [ele, ]
        d = {'action': 'move'}
        d.update(ele[-1])
        return d

    def build_grammars(self):
        pass

    def bind_parse_actions(self):
        pass
    def bind_grammar_actions(self):
        pass
    def __init__(self):
        self.bindParseActions()
        self.build_grammars()

    def parse(self,s):
        self.program.parseString(s)
