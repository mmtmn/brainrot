import re

class BrainrotLexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.keywords = {
            'yap', 'beta', 'sigma', 'vibe', 'stack', 'sauce', 'quote', 'squad', 'facts',
            'vibe check', 'bro did not pass', 'bussin\'', 'hits different', 'hot take',
            'main character', 'dms', 'slide into dms', 'slide back', 'understood the assignment',
            'flex', 'left on read', 'drip', 'lack', 'combo', 'ratio', 'no cap', 'cap',
            'squad goals', 'blud', 'highkey', 'lowkey', 'guarded af', 'cook', 'cooked',
            'yeet', 'red flag', 'send it', 'caught in 4k', 'last chance bro'
        }
        self.tokenize()

    def tokenize(self):
        words = re.split(r'(\s+|[{}()])', self.code)
        for word in words:
            word = word.strip()
            if word in self.keywords:
                self.tokens.append(('KEYWORD', word))
            elif re.match(r'^\d+(\.\d+)?$', word):  # Integer or double
                self.tokens.append(('NUMBER', float(word) if '.' in word else int(word)))
            elif word.startswith('"') and word.endswith('"'):  # String
                self.tokens.append(('STRING', word[1:-1]))
            elif word:
                self.tokens.append(('IDENTIFIER', word))

    def get_tokens(self):
        return self.tokens
