import sys
from lexer import BrainrotLexer
from parser import BrainrotParser
from interpreter import BrainrotInterpreter

def main():
    if len(sys.argv) < 2:
        print("Usage: python brainrot.py <filename>")
        return

    filename = sys.argv[1]
    with open(filename, 'r') as file:
        code = file.read()

    lexer = BrainrotLexer(code)
    tokens = lexer.get_tokens()

    parser = BrainrotParser(tokens)
    ast = parser.parse()

    interpreter = BrainrotInterpreter(ast)
    interpreter.interpret()

if __name__ == "__main__":
    main()
