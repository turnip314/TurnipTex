import Parsing.Parser as p
import Parsing.Grammar as g

TexCFG = g.Grammar({
        "Tex": [
            ["Expr"]
        ],
        "Expr": [
            ["CMD", "Expr"],
            ["POW", "Expr"],
            ["SUB", "Expr"],
            ["Word", "Expr"],
            ["PAREN", "Expr"],
            [],
        ],
        "PAREN": [
            ["(", "Expr", ")"]
        ],
        "CMD": [
            ["cmd"],
            ["cmd", "{", "Expr", "}"],
            ["cmd", "{", "Expr", "}", "{", "Expr", "}"]
        ],
        "POW": [
            ["BASE", "^x"],
            ["BASE", "^{", "Expr", "}"]
        ],
        "SUB": [
            ["BASE", "_x"],
            ["BASE", "_{", "Expr", "}"]
        ],
        "BASE": [
            ["text"],
            ["PAREN"],
        ],
        "Word": [
            ["text"],
            ["text", "Word"],
            ["\\infty", "Word"],

        ]
    }, "Tex"
)

class TexParser(p.Parser):
    def __init__(self):
        super(TexParser, self).__init__(TexCFG)


