class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()


s = Stack()
exp = input('Please enter the expression: ')
# (5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3)

for c in exp:
    if c == '(':
        s.push(1)
    if c == ')':
        if s.is_empty():
            is_balanced = False
            break
        s.pop()
    if c == '[':
        s.push(2)
    if c == ']':
        if s.is_empty():
            is_balanced = False
            break
        s.pop()
    if c == '{':
        s.push(3)
    if c == '}':
        if s.is_empty():
            is_balanced = False
            break
        s.pop()
else:
    if s.is_empty():
        is_balanced = True
    else:
        is_balanced = False

if is_balanced:
    print('Expression ', exp, ' is correctly parenthesized.')
else:
    print('Expression ', exp, ' is not correctly parenthesized.')
