import Parsing.Tex.TexScan as s
import Parsing.Tex.TexParser as p
import Math.Expr as exp
import Math.Fraction as frac
import Math.Power as pow
import Math.Sub as sub
import Math.Sum as sum
import Math.Text as txt
import Math.Word as word


class TexExpressionTreeGenerator:
    def __init__(self):
        pass

    def collapse(self, kind, tree):
        if tree.kind.get_kind != kind:
            return [tree]
        else:
            return [result for subtree in tree.children for result in self.collapse(kind, subtree)]

    def generate_expression_from_input(self, input_string):
        tokens = s.TexScan().scan(input_string)
        parsed_tree = p.TexParser().parse(tokens)
        return self.generate_expression_tree(parsed_tree[0])

    def generate_expression_tree(self, tree):
        if tree is None:
            return txt.Text("")

        if tree.kind.get_kind == "Expr":
            sub_expr_trees = self.collapse("Expr", tree)
            return exp.Expr([self.generate_expression_tree(t) for t in sub_expr_trees])

        elif tree.kind.get_kind == "CMD":
            """
            ["cmd"],
            ["cmd", "{", "Expr", "}"],
            ["cmd", "{", "Expr", "}", "{", "Expr", "}"]
            """
            cmd = tree.children[0].kind.get_lexeme
            sub_expr_one = tree.children[2] if len(tree.children) > 2 else None
            sub_expr_two = tree.children[5] if len(tree.children) > 5 else None
            if cmd == "\\frac":
                return frac.Fraction(
                    self.generate_expression_tree(sub_expr_one),
                    self.generate_expression_tree(sub_expr_two)
                )
            elif cmd == "\\sum":
                return sum.Sum(
                    self.generate_expression_tree(sub_expr_one),
                    self.generate_expression_tree(sub_expr_two)
                )

        elif tree.kind.get_kind == "POW":
            kind = tree.children[0].kind.get_kind
            if kind == "^x":
                return pow.Power(txt.Text(tree.children[0].kind.get_lexeme[1:]))  # ???
            elif kind == "^{":
                return pow.Power(
                    self.generate_expression_tree(tree.children[1])
                )

        elif tree.kind.get_kind == "SUB":
            kind = tree.children[0].kind.get_kind
            if kind == "_x":
                return sub.Sub(txt.Text(tree.children[0].kind.get_lexeme[1:]))  # ???
            elif kind == "_{":
                return sub.Sub(
                    self.generate_expression_tree(tree.children[1])
                )

        elif tree.kind.get_kind == "Word":
            sub_expr_trees = self.collapse("Word", tree)
            return word.Word([self.generate_expression_tree(t) for t in sub_expr_trees])

        else:
            return txt.Text(tree.kind.get_lexeme)