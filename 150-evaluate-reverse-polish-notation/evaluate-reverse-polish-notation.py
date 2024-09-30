class Solution:

    def compute(self, num1, num2, operator):
        result = 0
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        else:
            return int(num1 / num2)
        return result

    def evalRPN(self, tokens: List[str]) -> int:
        #stack to keep track of operated results
        stack = []
        for token in tokens:
            #if token is a number, push it onto the stack
            if token not in ["+", "-", "/", "*"]:
                stack.append(int(token))
                continue
            #if token is an operator, pop the last two numbers num2 first then num1, compute and push onto stack
            else:
                operator = token
                num2 = stack.pop()
                num1 = stack.pop()
                result = self.compute(num1, num2, operator)
                stack.append(int(result))
        #return the last pushed result by doing return stack.pop()
        return stack.pop()


            
