class Solution:
    def simplifyPath(self, path: str) -> str:
        #for path questions, always use a stack
        # if we have "..", we want to get rid of the part before, so we  pop from stack to get the  last value  removed
        # if we have "." or empty string, we dont want anything to be on stack
        #else if we have "..." or any or other legit part, we put that on stack
        #return the joined string with "/" in front
        stack = []
        for part in path.split("/"):
            if part == "..":
                if stack:
                    stack.pop()
            elif part == "." or  part  == "":
                continue
            else:
                stack.append(part)
        return "/" + "/".join(stack)
        