class Grammar:
    def __init__(self, productions, start):
        """
        :param grammar: Map[String, List[List[String]]]
        """
        self.productions = productions
        self.non_terminals = [p for p in productions]
        self.symbols = list(set(self.non_terminals + [s for production in productions.values()
                                                      for symbol_list in production for s in symbol_list]))
        self.terminals = list(set(self.symbols).difference(self.non_terminals))
        self.start = start
        assert start in productions

    def get_productions_expanding(self, non_terminal):
        """
        :param non_terminal: String
        :return: List[List[String]]
        """
        return self.productions[non_terminal]

    @property
    def get_productions(self):
        return self.productions

    @property
    def get_non_terminals(self):
        return self.non_terminals

    @property
    def get_terminals(self):
        return self.terminals

    @property
    def get_start(self):
        return self.start