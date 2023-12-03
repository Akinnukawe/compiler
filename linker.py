# Assuming ide.py provides an interface class called IDEInterface
from lexer import Lexer
from parser_1 import Parser
from IDE import IDEInterface

class Linker:
    def __init__(self, lexer, parser, interface):
        self.lexer = lexer
        self.parser = parser
        self.interface = interface

    def run(self):
        while True:
            source_code = self.interface.get_input()
            if source_code == "":
                break

            try:
                tokens = self.lexer.tokenize(source_code)
                parse_tree = self.parser.parse(tokens)
                self.interface.display_output(parse_tree)
            except Exception as e:
                self.interface.display_error(str(e))

if __name__ == '__main__':
    interface = IDEInterface(code_output)  # Pass the code_output Text widget as an argument
    lexer = Lexer()
    parser = Parser()
    linker = Linker(lexer, parser, interface)
    linker.run()