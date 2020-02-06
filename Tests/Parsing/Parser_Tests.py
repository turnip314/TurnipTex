import Tests.Tests as t
import Parsing.DFA as dfa
import Parsing.Tokenizer as sc
import Parsing.Tex.TexScan as ts
import Parsing.Tex.TexParser as tp
import Parsing.Parser as p
import Parsing.Grammar as g
import Parsing.Token as t

"""g = g.Grammar(
    {
        "Start": [
            ["A"]
        ],
        "A": [
            ["A", "x"],
            ["x"],
        ]
    },
    "Start"
)

def create_tokens(lst):
    return [t.Token(e) for e in lst]


parser = p.Parser(g)
result = parser.parse_CYK(create_tokens(['x', 'x', 'x']))
print(result)"""

my_input = """
\\frac{1}{2}
"""
texScan = ts.TexScan()
texParse = tp.TexParser()
result = texParse.parse(texScan.scan(my_input))
print(result)

1