from Parsing.DFA import DFA
from Parsing.Tokenizer import Scanner
from Parsing.Tex.TexScan import TexScan

states = ['start', '0', '1', '2']
start = 'start'
accepting = ['0']

def transition(state, next):
    if state == 'start':
        state = '0'

    state = (2 * int(state) + int(next))%3
    return str(state)

dfa = DFA(states, start, accepting, transition)

print(dfa.is_valid("110"))

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

dfa2 = DFA(states2, start2, accepting2, transition2)

scanner = Scanner(dfa2)
tokens = scanner.maximal_munch_scan("abaaaabbbbaa")
for token in tokens:
    print(token.get_lexeme)

texscan = TexScan()