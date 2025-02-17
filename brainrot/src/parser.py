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
        
        if token == ('KEYWORD', 'beta'):
            return self.parse_variable_declaration()
        elif token == ('KEYWORD', 'sigma'):
            return self.parse_constant_declaration()
        elif token == ('KEYWORD', 'vibe check'):
            return self.parse_if_statement()
        elif token == ('KEYWORD', 'bussin\''):
            return self.parse_while_loop()
        elif token == ('KEYWORD', 'flex'):
            return self.parse_flex_statement()
        elif token == ('KEYWORD', 'dms'):
            return self.parse_function_definition()
        elif token == ('KEYWORD', 'slide into dms'):
            return self.parse_function_call()
        elif token == ('KEYWORD', 'understood the assignment'):
            self.position += 1
            return ('exit',)
        else:
            raise SyntaxError(f"Unknown statement: {token}")
            
    def parse_variable_declaration(self):
        self.position += 1  # Skip 'beta'
        var_name = self.tokens[self.position][1]
        self.position += 1  # Move to the data type

        # Parse the data type (e.g., 'stack', 'vibe')
        var_type = self.tokens[self.position][1]
        self.position += 1

        if self.tokens[self.position][1] == '=':
            self.position += 1  # Skip '='
            value = self.tokens[self.position]
            self.position += 1
            return ('var_decl', var_name, var_type, value)
        else:
            raise SyntaxError("Expected '=' in variable declaration")


    def parse_constant_declaration(self):
        self.position += 1  # Skip 'sigma'
        const_name = self.tokens[self.position][1]
        self.position += 2  # Skip constant name and '='
        value = self.tokens[self.position][1]
        self.position += 1
        return ('const_decl', const_name, value)

    def parse_if_statement(self):
        self.position += 1  # Skip 'vibe check'
        self.position += 1  # Skip '('
        
        # Parse the condition, e.g., 'brain no cap 160'
        left_operand = self.tokens[self.position][1]
        self.position += 1  # Move to operator (e.g., 'no cap' or 'cap')
        
        operator = self.tokens[self.position][1]
        self.position += 1  # Move to right operand (e.g., 160)
        
        right_operand = self.tokens[self.position][1]
        self.position += 2  # Skip past ')' to start of body

        # Build the condition tuple
        condition = (operator, left_operand, right_operand)

        # Parse the body within braces '{...}'
        self.position += 1  # Skip '{'
        if_body = []
        while self.tokens[self.position][1] != '}':
            if_body.append(self.parse_statement())
        self.position += 1  # Skip '}'

        # Check for optional `else` clause (`bro did not pass`)
        else_body = None
        if self.position < len(self.tokens) and self.tokens[self.position][1] == 'bro did not pass':
            self.position += 1  # Skip 'bro did not pass'
            self.position += 1  # Skip '{'
            else_body = []
            while self.tokens[self.position][1] != '}':
                else_body.append(self.parse_statement())
            self.position += 1  # Skip '}'

        return ('if', condition, if_body, else_body)


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
