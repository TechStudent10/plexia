from lexer import Lexer, PLUS, MUL, DIV, MINUS, EQUALS, Variable, Number

class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.variables = {}

    def evaluate_expression(self, tokens):
        if len(tokens) == 1:
            return tokens[0].value

        # Get indexes of all operands
        op_indexes = []
        for i in range(len(tokens) - 1):
            token = tokens[i]
            if isinstance(token, PLUS) or isinstance(token, MINUS) or isinstance(token, MUL) or isinstance(token, DIV):
                op_indexes.append([i, token])
        
        # Loop over all indexes and complete operations
        current_value = 0
        for i in range(len(op_indexes)):
            op_index = op_indexes[i]
            val_1 = int(tokens[op_index[0] - 1].value)
            val_2 = int(tokens[op_index[0] + 1].value)
            token = op_index[1]

            if isinstance(token, PLUS):
                current_value = val_1 + val_2 if i == 0 else current_value + val_2
            elif isinstance(token, MINUS):
                current_value = val_1 - val_2 if i == 0 else current_value - val_2
            elif isinstance(token, MUL):
                current_value = val_1 * val_2 if i == 0 else current_value * val_2
            elif isinstance(token, DIV):
                current_value = val_1 / val_2 if i == 0 else current_value / val_2
        
        return current_value

    def get_value(self, tokens):
        # Only one variable
        if len(tokens) == 2:
            if isinstance(tokens[1], Variable):
                return self.variables[tokens[1].value]
        # Only Numbers
        if not any(isinstance(x, Variable) for x in tokens):
            _tokens = tokens[1:]
            if len(_tokens) <= 0:
                _tokens = tokens
            return self.evaluate_expression(_tokens)
        # Variables and numbers
        if any(isinstance(x, Variable) for x in tokens) and any(isinstance(x, Number) for x in tokens):
            final_token_list = []
            for token in tokens:
                if isinstance(token, Variable):
                    final_token_list.append(Number(self.variables[token.value]))
                else:
                    final_token_list.append(token)

            return self.evaluate_expression(final_token_list)
        # Only variables
        final_token_list = []
        for token in tokens:
            if isinstance(token, Variable):
                final_token_list.append(Number(self.variables[token.value]))
            else:
                final_token_list.append(token)
        return self.evaluate_expression(final_token_list)

    def parse(self, code):
        lines = code.split("\n")
        tokens = self.lexer.tokenize(lines)
        for tokenized_line in tokens:
            keyword = tokenized_line[0]
            if keyword.value == "calc":
                print(self.evaluate_expression(tokenized_line))
            elif keyword.value == "print":
                print(self.get_value(tokenized_line))
            elif isinstance(tokenized_line[1], EQUALS):
                del tokenized_line[0]
                del tokenized_line[0]
                self.variables[keyword.value] = self.get_value(tokenized_line)

if __name__ == "__main__":
    code = """#calc 2 + 2 * 5 / 10 * 20 + 1000
#calc 1 + 4
number = 1 + 3
print $number
print 2 + 5
print $number + 2
print $number * $number"""
    lexer = Lexer()
    parser = Parser(lexer)
    parser.parse(code)
