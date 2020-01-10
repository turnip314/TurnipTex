

class Token:
    def __init__(self, kind, lexeme):
        self.kind = kind
        self.lexeme = lexeme

    def get_kind(self):
        return self.kind

    def get_lexeme(self):
        return self.lexeme
