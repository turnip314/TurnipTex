import Parsing.Parser as p
import Parsing.Grammar as g

TexCFG = g.Grammar({
        "Tex": [
            ["Expr"]
        ],
        "Expr": [
            ["Sum", "Expr"],
            ["Frac", "Expr"],
            ["Pow", "Expr"],
            ["Lim", "Expr"],
            [";", "Expr"],
            ["Word", "Expr"],
            []
        ],
        "Sum": [
            ["\\sum"],
            ["\\sum", "_", "{", "Word", "}"],
            ["\\sum", "_", "{", "Word", "}", "^", "{", "Word", "}"]
        ],
        "Frac": [
            ["\\frac", "{", "Expr", "}", "{", "Expr", "}"]
        ],
        "Pow": [
            ["^", "{", "Expr", "}"],
            ["^", "Word"]
        ],
        "Lim": [
            ["\\lim"],
            ["\\lim", "_", "{", "Word", "}"]
        ],
        "Word": [
            ["text", "Word"],
            ["\\infty", "Word"]
        ]
    }, "Tex"
)

class TexParser(p.Parser):
    def __init__(self):
        super(TexParser, self).__init__(TexCFG)

