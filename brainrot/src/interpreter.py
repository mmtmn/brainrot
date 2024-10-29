class BrainrotInterpreter:
    def __init__(self, ast):
        self.ast = ast
        self.env = {}

    def interpret(self):
        for node in self.ast:
            self.execute(node)

    def execute(self, node):
        if node[0] == 'var_decl':
            self.env[node[1]] = node[2]
        elif node[0] == 'if':
            condition = node[1]
            if self.evaluate(condition):
                for stmt in node[2]:
                    self.execute(stmt)

    def evaluate(self, condition):
        return self.env.get(condition, False)  # Simplified
