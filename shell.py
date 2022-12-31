from lexer import Lexer
from lang_parser import Parser

if __name__ == '__main__':
    running = True
    lexer = Lexer()
    parser = Parser(lexer)

    print("Welcome to the Plexia interactive shell!\nType any valid line of code into the shell below.")
    while running:
        line = input(">> ")
        if line == "exit":
            running = False
            break
        else:
            parser.parse(line)
