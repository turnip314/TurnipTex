

class Scanner:
    def __init__(self, dfa):
        self.dfa = dfa

    def maximal_munch_scan(self, input_string):
        """
        String:param input_string:
        List[Tokens]:return:
        """
        from Parsing.Token import Token

        def scan(string):
            state = self.dfa.get_start
            acc = ""
            last_accepted_state = state
            last_accepted_string = acc
            for char in string:
                if not self.dfa.is_defined_at(state, char):
                    break
                else:
                    state = self.dfa.one_transition(state, char)
                    acc += char
                    if self.dfa.is_accepting_state(state):
                        last_accepted_string = acc
                        last_accepted_state = state

            return last_accepted_state, last_accepted_string

        tokens = []
        while input_string:
            state, result_string = scan(input_string)
            if not result_string:
                raise Exception("Invalid Scan")

            tokens.append(Token(state, result_string))
            input_string = input_string[len(result_string):]

        return tokens
