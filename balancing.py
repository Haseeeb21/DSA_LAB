from collections import deque  # Importing library

opening_brackets = ['[', '{', '(']  # Setting different barackets
closing_brackets = [']', '}', ')']


class is_Balanced:
    # Defining different functions of stack
    def __init__(self):
        self.container = deque()  # Constructor

    def push(self, val):
        self.container.append(val)  # Appending

    def pop(self):
        self.container.pop()  # Popping

    def isEmpty(self):
        if self.size() == 0:  # Checking for empty stack
            return True
        else:
            False

    def size(self):
        return len(self.container)  # Size of Stack

    def examine(self, check_expression):  # Checking function
        for brackets in check_expression:
            if brackets in opening_brackets:
                self.push(brackets)  # Push in Stack
            elif brackets in closing_brackets:
                location = closing_brackets.index(brackets)
                if (self.size() > 0) and (opening_brackets[location] == self.container[self.size() - 1]):
                    self.pop()  # Popping if conditions satisfied
                else:
                    return "False (Unbalanced)"
        if self.size() == 0:
            return "True (Balanced)"
        else:
            return "False (Unbalanced)"


self = is_Balanced()
expression = input("Enter Expression:- ")  # Enter Expression
print(expression, "is", self.examine(expression))
