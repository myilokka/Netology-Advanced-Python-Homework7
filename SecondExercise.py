class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack):
            return False
        return True

    def push(self, element):
        self.stack.append(element)

    def str_push(self, string):
        for element in string:
            self.push(element)

    def pop(self):
        return self.stack.pop(-1)

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


class HookStr:

    def __init__(self):
        self.input_stack = Stack()
        self.tmp_stack = Stack()

    def push(self, string):
        self.input_stack.str_push(string)

    def is_balanced(self):
        length = self.input_stack.size()
        if length % 2 == 0:
            for i in range(length):
                inp_peek = self.input_stack.peek()
                if inp_peek in '})]':
                    self.tmp_stack.push(self.input_stack.pop())
                    continue
                if inp_peek in '{[(' and self.tmp_stack.size() > 0:
                    tmp_peek = self.tmp_stack.peek()
                    if tmp_peek == '}' and inp_peek == '{':
                        self.tmp_stack.pop()
                        self.input_stack.pop()
                    elif tmp_peek == ']' and inp_peek == '[':
                        self.tmp_stack.pop()
                        self.input_stack.pop()
                    elif tmp_peek == ')' and inp_peek == '(':
                        self.tmp_stack.pop()
                        self.input_stack.pop()
                    else:
                        return 'Несбалансированно'

                else:
                    return 'Несбалансированно'

            return 'Сбалансированно'
        else:
            return 'Несбалансированно'


if __name__ == '__main__':
    string = "[()()()()({[]})(){}{(((())))}]"
    hook_str = HookStr()
    hook_str.push(string)
    print(hook_str.is_balanced())
