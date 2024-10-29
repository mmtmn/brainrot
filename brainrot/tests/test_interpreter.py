import unittest
from src.lexer import BrainrotLexer
from src.parser import BrainrotParser
from src.interpreter import BrainrotInterpreter
from io import StringIO
import sys

class TestBrainrotInterpreter(unittest.TestCase):
    def setUp(self):
        # Redirect stdout to capture prints (for testing flex output)
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        # Reset stdout
        sys.stdout = sys.__stdout__

    def test_variable_declaration(self):
        code = 'beta age stack = 25'
        lexer = BrainrotLexer(code)
        tokens = lexer.get_tokens()
        parser = BrainrotParser(tokens)
        ast = parser.parse()
        
        interpreter = BrainrotInterpreter(ast)
        interpreter.interpret()
        
        # Check if the variable 'age' is correctly set in the environment
        self.assertEqual(interpreter.env['age'], 25)

    def test_conditional_statement_true(self):
        code = '''
        beta age stack = 21
        vibe check (age no cap 21) {
            flex "Access granted"
        }
        '''
        lexer = BrainrotLexer(code)
        tokens = lexer.get_tokens()
        parser = BrainrotParser(tokens)
        ast = parser.parse()
        
        interpreter = BrainrotInterpreter(ast)
        interpreter.interpret()
        
        # Check if the correct output was printed
        self.assertIn("Access granted", self.held_output.getvalue())

    def test_conditional_statement_false(self):
        code = '''
        beta age stack = 18
        vibe check (age no cap 21) {
            flex "Access granted"
        } bro did not pass {
            flex "Access denied"
        }
        '''
        lexer = BrainrotLexer(code)
        tokens = lexer.get_tokens()
        parser = BrainrotParser(tokens)
        ast = parser.parse()
        
        interpreter = BrainrotInterpreter(ast)
        interpreter.interpret()
        
        # Check if the "else" branch executed correctly
        self.assertIn("Access denied", self.held_output.getvalue())

    def test_output_flex(self):
        code = 'flex "Hello, Brainrot!"'
        lexer = BrainrotLexer(code)
        tokens = lexer.get_tokens()
        parser = BrainrotParser(tokens)
        ast = parser.parse()
        
        interpreter = BrainrotInterpreter(ast)
        interpreter.interpret()
        
        # Verify that the correct string was output
        self.assertIn("Hello, Brainrot!", self.held_output.getvalue())

if __name__ == '__main__':
    unittest.main()
