from yatage.yatage_base.parser.GRAMMAR import normal_statement


class parser():
    def __init__(self,World):
        self.world = World
        self.program = normal_statement

    def parse(self,s):
        return self.program.parseString(s)

if __name__ == "__main__":
    p = parser(None)
    while True:
        print(p.parse(input('>')))