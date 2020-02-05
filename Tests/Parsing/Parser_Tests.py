import Tests.Tests as t
import Parsing.DFA as dfa
import Parsing.Scanner as sc
import Parsing.Tex.TexScan as ts
import Parsing.Parser as p
import Parsing.CFG as c
import Parsing.Token as t

cfg = c.CFG(
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


parser = p.Parser(cfg)
result = parser.parse_CYK(create_tokens(['x', 'x', 'x']))
print(result)