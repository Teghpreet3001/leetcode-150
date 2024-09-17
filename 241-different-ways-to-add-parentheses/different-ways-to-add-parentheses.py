class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # map = {}
        # if expression in map:
        #     return map[expression]
        result = []
        for i in range(len(expression)):
            char = expression[i]
            if char in ['+', '-', '*']:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for  l in left:
                    for r in right:
                        if char == "+":
                            result.append(l + r)
                        elif char == "-":
                            result.append(l - r)
                        elif char == "*":
                            result.append(l * r)
        if len(result) == 0:
            result.append(eval(expression))
        # map[expression] = result
        return result

                        