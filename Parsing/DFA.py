
class DFA:
    def __init__(self, states, start, accepting, transition):
        """
        List[String]:param states:
        String:param start:
        String:param accepting:
        Function[(String, Char) => String]:param transition:
        """
        self.states = states
        self.start = start
        self.accepting = accepting
        self.transition = transition

    @property
    def get_start(self):
        return self.start

    def is_accepting_state(self, state):
        return state in self.accepting

    def is_defined_at(self, state, next):
        return self.transition(state, next) is not None

    def one_transition(self, state, next):
        """
        String:param state: Current state
        String:return: New state after applying one step of transition to char
        """
        assert self.is_defined_at(state, next)
        return self.transition(state, next)

    def is_valid(self, input_string):
        """
        :param input_string: String to validate
        Boolean:return: If input_string satisfies the DFA
        """

        def validator(string, state):
            if not string:
                return state in self.accepting
            elif self.is_defined_at(state, string[0]):
                return validator(string[1:], self.one_transition(state, string[0]))
            else:
                return False

        return validator(input_string, self.get_start)

