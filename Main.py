from Parsing.DFA import DFA

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