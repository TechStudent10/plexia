from string import digits as DIGITS
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

class Lexer:
    def __init__(self):
        pass

    def tokenize(self, lines):
        tokens = []

        for line in lines:
            if line[0] == "#": continue
            if len(line) == 0: continue
            tokenized_line = []
            words = line.split(" ")
            keyword = words[0]
            tokenized_line.append(Keyword(keyword))
            
            for word in words:
                if word == "(":
                    tokenized_line.append(LPARAN())
                elif word == ")":
                    tokenized_line.append(RPARAN())
                elif word == "+":
                    tokenized_line.append(PLUS())
                elif word == "-":
                    tokenized_line.append(MINUS())
                elif word == "/":
                    tokenized_line.append(DIV())
                elif word == "*":
                    tokenized_line.append(MUL())
                elif word == "=":
                    tokenized_line.append(EQUALS())
                elif word[0] == "$":
                    tokenized_line.append(Variable(word[1:]))
                else:
                    try:
                        int(word)
                        tokenized_line.append(Number(word))
                    except ValueError:
                        try:
                            float(word)
                            tokenized_line.append(Number(str(math.floor(int(word)))))
                        except ValueError:
                            pass
        
            tokens.append(tokenized_line)

        return tokens

if __name__ == "__main__":
    line = ["calc 2 + 2 * 5"]
    lexer = Lexer()
    print(lexer.tokenize(line))
