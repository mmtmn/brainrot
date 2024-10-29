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
        elif token[1] == 'vibe check':
            return self.parse_if_statement()
        else:
            raise SyntaxError(f"Unknown statement: {token}")

    def parse_variable_declaration(self):
        self.position += 1  # Skip 'beta'
        var_name = self.tokens[self.position][1]
        self.position += 2  # Skip variable name and '='
        value = self.tokens[self.position][1]
        self.position += 1
        return ('var_decl', var_name, value)

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
