from lexer import Lexer, Token

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_index = 0

    def current_token(self):
        if self.current_index < len(self.tokens):
            return self.tokens[self.current_index]
        else:
            return Token('EOF', None)

    def consume(self, expected_type):
        if self.current_token().type == expected_type:
            current_token = self.current_token()
            self.current_index += 1
            return current_token
        else:
            raise ValueError(f"Expected token type {expected_type} but got {self.current_token().type}")

    def parse_number(self):
        token = self.current_token()
        if token.type == 'INTEGER' or token.type == 'FLOAT':
            self.consume(token.type)
            return token
        else:
            raise ValueError(f"Expected INTEGER or FLOAT but got {token.type}")

    def parse_term(self):
        token = self.current_token()
        if token.type in ('INTEGER', 'FLOAT'):
            return self.parse_number()
        elif token.type == 'LPAREN':
            self.consume('LPAREN')
            expr = self.parse_expression()
            self.consume('RPAREN')
            return expr
        else:
            raise ValueError(f"Unexpected token {token.type}")

    def parse_factor(self):
        left = self.parse_term()
        while self.current_token().type in ('MULTIPLY', 'DIVIDE'):
            operator = self.consume(self.current_token().type)
            right = self.parse_term()
            left = ('BINARY_OP', operator, left, right)
        return left

    def parse_expression(self):
        left = self.parse_factor()
        while self.current_token().type in ('PLUS', 'MINUS'):
            operator = self.consume(self.current_token().type)
            right = self.parse_factor()
            left = ('BINARY_OP', operator, left, right)
        return left

    def parse(self):
        return self.parse_expression()

# Usage Example
if __name__ == '__main__':
    source_code = "3.14 * (2 + 1) - 2 / 4"
    lexer = Lexer(source_code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    parse_tree = parser.parse()
    print(parse_tree)