import Tests.Tests as t
import Parsing.DFA as dfa
import Parsing.Tokenizer as sc
import Parsing.Tex.TexScan as ts

class Scanner_Tests(t.Tests):
    def __init__(self):
        self.test_methods = [
            self.test_basic,
            self.test_tex_scan,
        ]

    def test_basic(self):
        states2 = ['start', 'a', 'b']
        start2 = 'start'
        accepting2 = ['a', 'b']

        def transition2(state, next):
            if state == 'start':
                if next == 'a':
                    return 'a'
            if state == 'a':
                if next == 'b':
                    return 'b'
            if state == 'b':
                if next == 'a':
                    return 'a'
                elif next == 'b':
                    return 'b'
            return None

        dfa2 = dfa.DFA(states2, start2, accepting2, transition2)

        tokenizer = sc.Tokenizer(dfa2)
        tokens = tokenizer.maximal_munch_scan("abaaaabbbbaa")
        for token in tokens:
            print(token.get_lexeme)

    def test_tex_scan(self):
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
        text_scan = ts.TexScan()
        input_string = "\\frac{\\sum{1}{2}}  _ "
        result = text_scan.scan(input_string)
        for token in result:
            print(token.get_kind, token.get_lexeme)

if __name__ == "__main__":
    tests = Scanner_Tests()
    tests.run_tests()