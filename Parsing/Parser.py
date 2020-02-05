import Parsing.CFG as cfg
import Parsing.Token as t

class Tree:
    def __init__(self, kind, children=[]):
        self.kind = kind
        self.children = children

    def __str__(self):
        return 1


class Parser:
    def __init__(self, CFG):
        """
        :param CFG: CFG
        """
        self.CFG = CFG
        self.parser = self.parse_CYK

    def parse_CYK(self, tokens):
        """
        :param tokens: List[Symbols]
        :return: Tree
        """

        def get_key(lhs, pos, length):
            return ",".join(lhs) + "|" + str(pos) + "|" + str(length)

        memo = {}

        def parse(lhs, pos, length):
            """
            :param lhs: List[String]
            :param pos: int
            :param length: int
            :return:
            """
            print(lhs, pos, length)
            if get_key(lhs, pos, length) in memo:
                return memo[get_key(lhs, pos, length)]
            memo[get_key(lhs, pos, length)] = None
            result = None
            if not lhs:
                if not length:
                    result = []
            elif lhs[0] in self.CFG.terminals:
                if length:
                    if tokens[pos].get_kind == lhs[0] and parse(lhs[1:], pos+1, length-1) is not None:
                        result = [Tree(tokens[pos])] + parse(lhs[1:], pos+1, length-1)
            elif len(lhs) == 1 and lhs[0] in self.CFG.non_terminals:
                for production in self.CFG.get_productions_expanding(lhs[0]):
                    if parse(production, pos, length) is not None:
                        result = [Tree(t.Token(lhs[0]), parse(production, pos, length))]
            else:
                assert lhs[0] in self.CFG.non_terminals
                for i in range(length+1):
                    if parse([lhs[0]], pos, i) is not None and parse(lhs[1:], pos+i, length-i) is not None:
                        result = parse([lhs[0]], pos, i) + parse(lhs[1:], pos+i, length-i)

            memo[get_key(lhs, pos, length)] = result
            return result

        result = parse(self.CFG.get_productions_expanding(self.CFG.start)[0], 0, len(tokens))
        print(memo)
        return result