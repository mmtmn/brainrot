class BrainrotInterpreter:
    def __init__(self, ast):
        self.ast = ast
        self.env = {}

    def interpret(self):
        for node in self.ast:
            self.execute(node)

    def execute(self, node):
        if node[0] == 'var_decl':
            var_name = node[1]
            var_type = node[2]
            value = node[3][1]  # Extract the actual value from the token tuple

            # Handle types (stack = int, vibe = bool, etc.)
            if var_type == 'stack':
                self.env[var_name] = int(value)
            elif var_type == 'vibe':
                self.env[var_name] = bool(value)
            elif var_type == 'sauce':
                self.env[var_name] = float(value)
            elif var_type == 'quote':
                self.env[var_name] = str(value)
            else:
                raise TypeError(f"Unknown type '{var_type}' for variable '{var_name}'")
        
        elif node[0] == 'if':
            condition, if_body, else_body = node[1], node[2], node[3]
            if self.evaluate(condition):
                for stmt in if_body:
                    self.execute(stmt)
            elif else_body:  # Execute `else` block if condition is false and else_body exists
                for stmt in else_body:
                    self.execute(stmt)
        elif node[0] == 'flex':
            print(node[1])  # Print message


    def evaluate(self, condition):
        operator, left_operand, right_operand = condition
        left_value = self.env.get(left_operand)
        right_value = int(right_operand) if right_operand.isdigit() else right_operand

        if operator == 'no cap':
            return left_value == right_value
        elif operator == 'cap':
            return left_value != right_value
        return False
