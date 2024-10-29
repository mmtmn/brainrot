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
        elif node[0] == 'const_decl':
            self.env[node[1]] = node[2]
        elif node[0] == 'if':
            condition = node[1]
            if self.evaluate(condition):
                for stmt in node[2]:
                    self.execute(stmt)
        elif node[0] == 'while':
            condition = node[1]
            while self.evaluate(condition):
                for stmt in node[2]:
                    self.execute(stmt)
        elif node[0] == 'flex':
            print(node[1])  # Print message
        elif node[0] == 'function_def':
            func_name = node[1]
            self.env[func_name] = node
        elif node[0] == 'function_call':
            func_name = node[1]
            func_node = self.env.get(func_name)
            if func_node:
                self.execute(func_node)
            else:
                print(f"Error: function '{func_name}' not found")
        elif node[0] == 'exit':  # Handle program completion
            exit(0)

    def evaluate(self, condition):
        return self.env.get(condition, False)  # Simplified evaluation
