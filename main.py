from lexer import Lexer
from lang_parser import Parser
from argparse import ArgumentParser, FileType

argument_parser = ArgumentParser(
    prog="main.py",
    description="Main runner file for Plexia",
    epilog="Happy coding :D"
)
argument_parser.add_argument("file", type=FileType("r"))

args = argument_parser.parse_args()

lexer = Lexer()
parser = Parser(lexer)
parser.parse(args.file.read())
