import unittest
from src.lexer import BrainrotLexer

class TestBrainrotLexer(unittest.TestCase):
    def test_lexer_tokens(self):
        code = 'beta age stack = 25'
        lexer = BrainrotLexer(code)
        tokens = lexer.get_tokens()
        expected_tokens = [
            ('KEYWORD', 'beta'),
            ('IDENTIFIER', 'age'),
            ('KEYWORD', 'stack'),
            ('OPERATOR', '='),
            ('NUMBER', 25)
        ]
        self.assertEqual(tokens, expected_tokens)

if __name__ == '__main__':
    unittest.main()
