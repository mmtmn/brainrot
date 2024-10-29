import unittest
from src.lexer import BrainrotLexer
from src.parser import BrainrotParser

class TestBrainrotParser(unittest.TestCase):
    def test_parse_variable_declaration(self):
        code = 'beta age stack = 25'
        lexer = BrainrotLexer(code)
        tokens = lexer.get_tokens()
        parser = BrainrotParser(tokens)
        ast = parser.parse()
        expected_ast = [('var_decl', 'age', 25)]
        self.assertEqual(ast, expected_ast)

if __name__ == '__main__':
    unittest.main()
