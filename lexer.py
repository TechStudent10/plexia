from string import digits as DIGITS, ascii_letters
import math

class Token:
    token_type = "Generic"
    
    def __repr__(self):
        return f"<{self.token_type}>"

class TokenWithValue:
    token_type = "GenericWithValue"
    
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"<{self.token_type} value={self.value}>"

class LPARAN(Token):
    token_type = "LPARAN"

class RPARAN(Token):
    token_type = "RPARAN"

class PLUS(Token):
    token_type = "PLUS"

class MINUS(Token):
    token_type = "MINUS"

class DIV(Token):
    token_type = "DIV"

class MUL(Token):
    token_type = "MUL"

class NEWLINE(Token):
    token_type = "NEWLINE"

class EQUALS(Token):
    token_type = "EQUALS"

class Number(TokenWithValue):
    token_type = "NUMBER"

class Keyword(TokenWithValue):
    token_type = "KEYWORD"

class Variable(TokenWithValue):
    token_type = "VARIABLE"

class String(TokenWithValue):
    token_type = "STRING"

class Lexer:
    def __init__(self):
        pass

    def tokenize(self, lines):
        tokens = []

        currently_in_quotes = False
        current_string = ""
        for line in lines:
            if len(line) == 0 or line == "": continue
            if line[0] == "#": continue
            tokenized_line = []
            words = line.split(" ")
            keyword = words[0]
            tokenized_line.append(Keyword(keyword))
            
            for word in words:
                token = None

                if currently_in_quotes:
                    current_string = current_string + " " + (word[:-1] if word.endswith("\"") or word.endswith("'") else word)
                    # print("c", current_string)
                    # continue

                if word == " ":
                    pass
                elif word == "(":
                    token = LPARAN()
                elif word == ")":
                    token = RPARAN()
                elif word == "+":
                    token = PLUS()
                elif word == "-":
                    token = MINUS()
                elif word == "/":
                    token =  DIV()
                elif word == "*":
                    token = MUL()
                elif word == "=":
                    token = EQUALS()
                elif word.startswith("$"):
                    token = Variable(word[1:])
                elif word.startswith("\"") or word.startswith("'"):
                    if currently_in_quotes == False:
                        if word.endswith("\"") or word.endswith("'"):
                            token = String(word[:-1][1:])
                            currently_in_quotes = False
                        else:
                            currently_in_quotes = True
                            current_string = word[1:]
                elif word.endswith("\"") or word.endswith("'"):
                    token = String(current_string)
                    currently_in_quotes = False
                else:
                    try:
                        int(word)
                        token = Number(word)
                    except ValueError:
                        try:
                            float(word)
                            token = Number(str(math.floor(int(word))))
                        except ValueError:
                            pass

                if token:
                    if isinstance(token, list):
                        for t in token:
                            tokenized_line.append(t)
                    else:
                        tokenized_line.append(token)
        
            tokens.append(tokenized_line)

        return tokens

if __name__ == "__main__":
    line = ["greeting = \"Hi\""]
    lexer = Lexer()
    print(lexer.tokenize(line))
