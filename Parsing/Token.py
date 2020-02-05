

class Token:
    def __init__(self, kind, lexeme = ""):
        self.kind = kind
        self.lexeme = lexeme

    @property
    def get_kind(self):
        return self.kind

    @property
    def get_lexeme(self):
        return self.lexeme

    def set_kind(self, new_kind):
        self.kind = new_kind

    def set_lexeme(self, new_lexeme):
        self.lexeme = new_lexeme