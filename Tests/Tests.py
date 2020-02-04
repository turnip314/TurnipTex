class Tests:
    def __init__(self):
        self.test_methods = []

    def run_tests(self):
        for test in self.test_methods:
            test()
