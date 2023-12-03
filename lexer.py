import re

# Define the token types and their regex patterns
TOKEN_TYPES = {
    'FLOAT': r'\b\d*\.\d+\b',  
    'INTEGER': r'\b\d+\b',
    'IDENTIFIER': r'\b[a-zA-Z_]\w*\b',
    'PLUS': r'\+',
    'MINUS': r'-',
    'MULTIPLY': r'\*',
    'DIVIDE': r'/',
    'LPAREN': r'\(',
    'RPAREN': r'\)',
    'SEMICOLON': r';',
    'WHITESPACE': r'\s+',
    'ASSIGN': r'='
}

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)})"

# Lexer class to tokenize source code
class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []
        self.current_index = 0
        # Precompile the regular expressions
        self.regex_patterns = {type_: re.compile(pattern) for type_, pattern in TOKEN_TYPES.items()}

    # ... (rest of the Lexer class)
    def tokenize(self):
        while self.current_index < len(self.source_code):
            match = None
            for token_type, regex in self.regex_patterns.items():
                match = regex.match(self.source_code, self.current_index)
                if match:
                    value = match.group(0)
                    if token_type != 'WHITESPACE':  # Skip whitespace
                        self.tokens.append(Token(token_type, value))
                    self.current_index = match.end()
                    break
            if not match:
                # Print the problematic part of the source code
                print(f"Problematic character at index {self.current_index}: '{self.source_code[self.current_index]}'")
                raise ValueError(f"Unknown token at index {self.current_index}")
        return self.tokens

# Example usage
if __name__ == '__main__':
    source_code = "x = 3.14; y = x * 2;"
    lexer = Lexer(source_code)
    tokens = lexer.tokenize()
    for token in tokens:
        print(token)