import Parsing.Tokenizer as t
import Parsing.DFA as DFA

"""
TexScan Language:
\\[without _\\{}^]*      : cmd
_                      : _
{                      : {
}                      : }
^                      : ^
whitespace, tab, etc   : space
[without _\\{}^]*       : text
"""


class TokenKinds:
    CMD          = "cmd"
    UNDERSCORE   = "_"
    LEFT_BRACE   = "{"
    RIGHT_BRACE  = "}"
    UP_ARROW     = "^"
    SPACE        = "space"
    TEXT         = "text"

class TexScan(t.Tokenizer):
    def __init__(self):
        self.valid_cmds = [
            "frac",
            "sum"
        ]

        states = ['start', 'cmd', '_', '^', '{', '}', 'space', 'text']
        start = 'start'
        accepting = ['cmd', '_', '^', '{', '}', 'space', 'text']

        def transition(state, next):
            if state == 'start':
                if next == '\\':
                    return 'cmd'
                elif next == '_':
                    return '_'
                elif next == '^':
                    return '^'
                elif next == '{':
                    return '{'
                elif next == '}':
                    return '}'
                elif next in " ', '\t', '\n":
                    return 'space'
                else:
                    return 'text'
            elif state == 'cmd':
                if next not in "\\ \t\n_^{}":
                    return 'cmd'
            elif state == 'space':
                if next in [' \t\n']:
                    return 'space'
            elif state == 'text':
                if state not in "\\ \t\n_^{}":
                    return 'text'
            return None

        super(TexScan, self).__init__(DFA.DFA(states, start, accepting, transition))

    def scan(self, input_string):
        """
        Returns a list of tokens given a tex input. Removes anything that's unnecessary, including whitespaces, tabs,
        etc. Also removes the backslash from cmd names.
        :param input_string: String
        :return: List[Token]
        """

        tokens = self.maximal_munch_scan(input_string)
        tokens = [token for token in tokens if token.get_kind != TokenKinds.SPACE]
        for token in tokens:
            if token.get_kind == TokenKinds.CMD:
                assert token.get_lexeme[0] == "\\"
                token.set_lexeme(token.get_lexeme[1:])
                assert token.get_lexeme in self.valid_cmds

        return tokens
