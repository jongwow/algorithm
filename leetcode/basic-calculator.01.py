class Solution:
    def parse(self, s: str):
        tokens = []
        idx = 0
        while idx < len(s):
            if s[idx] == '+' or s[idx] == '-':
                tokens.append(s[idx])
                idx += 1
            elif s[idx].isdigit():
                num = int(s[idx])
                idx += 1
                while idx < len(s) and s[idx].isdigit():
                    num *= 10
                    num += int(s[idx])
                    idx += 1
                tokens.append(num)
            elif s[idx] == '(' or s[idx] == ')':
                tokens.append(s[idx])
                idx += 1
            else:
                idx += 1
        return tokens

    def calculateTokens(self, tokens) -> int:
        if len(tokens) == 1:
            return tokens[0]
        if len(tokens) == 2:
            if tokens[0] == '+':
                return tokens[1]
            if tokens[1] == '-':
                return -tokens[1]
        if len(tokens) == 3:
            if type(tokens[0]) == int:
                if tokens[1] == '+':
                    return tokens[0]+tokens[2]
                else:
                    return tokens[0]-tokens[2]
            if type(tokens[0]) == '(':
                return tokens[1]
        stack = []
        idx = 0
        while idx < len(tokens):
            if tokens[idx] == '(':
                start_index = idx+1
                brackets = 1
                idx += 1
                while brackets > 0:
                    if tokens[idx] == '(':
                        brackets += 1
                    if tokens[idx] == ')':
                        brackets -= 1
                    idx += 1
                sub_result = self.calculateTokens(tokens[start_index:idx-1])
                stack.append(sub_result)
            else:  # operator or integer
                stack.append(tokens[idx])
                idx += 1
        result = self.evaluateTokens(stack)
        return result

    def calculateTokensV2(self, tokens) -> int:
        if len(tokens) == 1:
            return tokens[0]
        if len(tokens) == 2:
            if tokens[0] == '+':
                return tokens[1]
            if tokens[1] == '-':
                return -tokens[1]
        if len(tokens) == 3:
            if type(tokens[0]) == int:
                if tokens[1] == '+':
                    return tokens[0]+tokens[2]
                else:
                    return tokens[0]-tokens[2]
            if type(tokens[0]) == '(':
                return tokens[1]
        stack = []
        idx = 0
        while idx < len(tokens):
            if tokens[idx] == '(':
                sub_stack = []
                while tokens[idx] != ')':
                    idx += 1
                    if tokens[idx] == ')':
                        sub_token = sub_stack.pop()
                        break
                    sub_stack.append(tokens[idx])
                    idx += 1
                sub_stack.pop()  # remove last bracket
                sub_result = self.calculateTokensV2(sub_stack)
                stack.append(sub_result)
            else:  # operator or integer
                stack.append(tokens[idx])
                idx += 1
        result = self.evaluateTokens(stack)
        return result

    def evaluateTokens(self, tokens) -> int:
        if len(tokens) == 1:
            return tokens[0]
        if len(tokens) == 2:  # [-,int] 밖에 없어야함.
            if tokens[0] == '-':
                return -tokens[1]
            else:
                return 0
        tokens.reverse()
        while len(tokens) > 1:
            a_token = tokens.pop()
            if a_token == '-':
                b_token = tokens.pop()
                tokens.append(-b_token)
                continue
            operator = tokens.pop()
            b_token = tokens.pop()
            if operator == '+':
                c_token = a_token + b_token
            else:
                c_token = a_token - b_token
            tokens.append(c_token)
        return tokens[0]

    def calculate(self, s: str) -> int:
        tokens = self.parse(s)
        result = self.calculateTokens(tokens)
        return result


class SolutionV2:
    def parse(self, s: str):
        tokens = []
        idx = 0
        while idx < len(s):
            if s[idx] == '+' or s[idx] == '-':
                tokens.append(s[idx])
                idx += 1
            elif s[idx].isdigit():
                num = int(s[idx])
                idx += 1
                while idx < len(s) and s[idx].isdigit():
                    num *= 10
                    num += int(s[idx])
                    idx += 1
                tokens.append(num)
            elif s[idx] == '(' or s[idx] == ')':
                tokens.append(s[idx])
                idx += 1
            else:
                idx += 1
        return tokens

    def isOperator(self, s):
        if s == '+' or s == '-':
            return True
        return False

    def isDigit(self, s):
        if type(s) == int:
            return True
        return False

    def evaluate(self, tokens):
        while len(tokens) > 1:
            token = tokens.pop()
            if self.isDigit(token):
                pass
            elif self.isOperator(token):
                pass
            elif self == ')':
                pass
        return tokens[0]

    def calculate(self, s: str) -> int:
        tokens = self.parse(s)
        tokens.reverse()
        result = self.evaluate(tokens)
        return result


tcs = [
    "1 + 1",
    " 2-1 + 2 ",
    "(1+(4+5+2)-3)+(6+8)",
    "-2+ 1",
]

for tc in tcs:
    result = Solution().calculate(tc)
    print(result)
