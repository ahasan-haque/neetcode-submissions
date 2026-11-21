class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for letter in s:
            if letter in ['(', '{', '[']:
                stack.append(letter)

            elif letter == ')':
                if stack and  stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(letter)
            elif letter == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(letter)

            elif letter == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(letter)

        return not stack
