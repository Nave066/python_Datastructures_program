class Stack(object):
    def __init__(self):
        self.values = []  # Constructor initialize the string values inside a list

    def push(self, value):
        """
        :param value: Each letter from the string
        :return: Nothing returned, The value is appended in the stack
        """
        self.values.append(value)

    def pop(self):
        """
            Here the last letter added gets popped out
            :return: The popped value gets returned.
        """
        return self.values.pop()


class Queue(object):
    def __init__(self):
        self.values = []

    def push(self, value):
        """
        :param value: The value from the string gets appended into a list
        :return: The value gets appended and nothing returns
        """
        self.values.append(value)

    def pop(self):
        """
        :return: The First element in the list gets popped, Because it is queue.
        """
        return self.values.pop(0)  # According to queue, the first element added will be popped first


stack = Stack()  # Declaration of stack and queue list
queue = Queue()


class PalindromeChecker(object):
    """
    Checks if a word is a palindrome or not
    using two
    """

    def __init__(self, word):
        self.word = word
        self.queue = Queue()
        self.stack = Stack()

    def check_palindrome(self):
        for letter in self.word:
            self.queue.push(letter)
            self.stack.push(letter)
        for i in range(len(self.word)):
            if self.queue.pop() != self.stack.pop():
                return False
        return True


# Driver Code
if __name__ == '__main__':
    input_string_by_user = input("Enter the String to check for palindrome:")
    result_output = PalindromeChecker(input_string_by_user)
    if result_output.check_palindrome():
        print(input_string_by_user, " is a palindrome")
    else:
        print(input_string_by_user, " is not a palindrome")