class BrainrotParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def parse(self):
        ast = []
        while self.position < len(self.tokens):
            ast.append(self.parse_statement())
        return ast

    def parse_statement(self):
        token = self.tokens[self.position]
        
        if token[1] == 'beta':
            return self.parse_variable_declaration()
        elif token[1] == 'sigma':
            return self.parse_constant_declaration()
        elif token[1] == 'vibe check':
            return self.parse_if_statement()
        elif token[1] == 'bussin\'':
            return self.parse_while_loop()
        elif token[1] == 'flex':
            return self.parse_flex_statement()
        elif token[1] == 'dms':
            return self.parse_function_definition()
        elif token[1] == 'slide into dms':
            return self.parse_function_call()
        elif token[1] == 'understood the assignment':  # Handle program completion
            self.position += 1
            return ('exit',)
        else:
            raise SyntaxError(f"Unknown statement: {token}")

            token = self.tokens[self.position]
            
            if token[1] == 'beta':
                return self.parse_variable_declaration()
            elif token[1] == 'sigma':
                return self.parse_constant_declaration()
            elif token[1] == 'vibe check':
                return self.parse_if_statement()
            elif token[1] == 'bussin\'':
                return self.parse_while_loop()
            elif token[1] == 'flex':
                return self.parse_flex_statement()
            elif token[1] == 'dms':
                return self.parse_function_definition()
            elif token[1] == 'slide into dms':
                return self.parse_function_call()
            else:
                raise SyntaxError(f"Unknown statement: {token}")

    def parse_variable_declaration(self):
        self.position += 1  # Skip 'beta'
        var_name = self.tokens[self.position][1]
        self.position += 2  # Skip variable name and '='
        value = self.tokens[self.position][1]
        self.position += 1
        return ('var_decl', var_name, value)

    def parse_constant_declaration(self):
        self.position += 1  # Skip 'sigma'
        const_name = self.tokens[self.position][1]
        self.position += 2  # Skip constant name and '='
        value = self.tokens[self.position][1]
        self.position += 1
        return ('const_decl', const_name, value)

    def parse_if_statement(self):
        self.position += 1  # Skip 'vibe check'
        condition = self.tokens[self.position][1]
        self.position += 1  # Skip condition
        self.position += 1  # Skip '{'
        body = []
        while self.tokens[self.position][1] != '}':
            body.append(self.parse_statement())
        self.position += 1  # Skip '}'
        return ('if', condition, body)

    def parse_while_loop(self):
        self.position += 1  # Skip 'bussin\''
        condition = self.tokens[self.position][1]
        self.position += 1  # Skip condition
        self.position += 1  # Skip '{'
        body = []
        while self.tokens[self.position][1] != '}':
            body.append(self.parse_statement())
        self.position += 1  # Skip '}'
        return ('while', condition, body)

    def parse_flex_statement(self):
        self.position += 1  # Skip 'flex'
        message = self.tokens[self.position][1]
        self.position += 1
        return ('flex', message)

    def parse_function_definition(self):
        self.position += 1  # Skip 'dms'
        func_name = self.tokens[self.position][1]
        self.position += 1  # Move to the next token
        return ('function_def', func_name)

    def parse_function_call(self):
        self.position += 1  # Skip 'slide into dms'
        func_name = self.tokens[self.position][1]
        self.position += 1
        return ('function_call', func_name)
