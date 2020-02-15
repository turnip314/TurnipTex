import Parsing.Tex.TexExpressionTreeGenerator as g

my_input = """
\\frac{a_1}{2^{\\frac{1}{2}}}
"""

generator = g.TexExpressionTreeGenerator()
result = generator.generate_expression_from_input(my_input)
1
1
# print(result)
