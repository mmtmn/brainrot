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
        # Ensure multi-word keywords are prioritized and matched fully
        multi_word_keywords = [kw for kw in self.keywords if ' ' in kw]
        single_word_keywords = [kw for kw in self.keywords if ' ' not in kw]
        
        # Compile a regex pattern to match multi-word keywords first, then single words and numbers
        pattern = (
            r'\b(?:' + '|'.join(re.escape(kw) for kw in multi_word_keywords) + r')\b|'
            r'\b(?:' + '|'.join(re.escape(kw) for kw in single_word_keywords) + r')\b|'
            r'"[^"]*"|\S+'
        )
        
        words = re.findall(pattern, self.code)

        for word in words:
            word = word.strip()
            if word in self.keywords:
                self.tokens.append(('KEYWORD', word))
            elif word.startswith('"') and word.endswith('"'):  # Entire string within quotes
                self.tokens.append(('STRING', word[1:-1]))  # Remove surrounding quotes
            elif re.match(r'^\d+(\.\d+)?$', word):  # Integer or double
                self.tokens.append(('NUMBER', float(word) if '.' in word else int(word)))
            elif word in ('no cap', 'cap'):  # Condition operators
                self.tokens.append(('OPERATOR', word))
            else:
                self.tokens.append(('IDENTIFIER', word))

    def get_tokens(self):
        return self.tokens
