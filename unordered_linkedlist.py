class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def display_all(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None:
                current = current.next_node
            current.next_node = new_node

    def file_display(self):
        current = self.head
        temp = ""
        while current:
            # print(current.data, end = ' ')
            temp = temp + current.data + " "
            current = current.get_next()
        return temp

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        return found

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


# Main Code execution starts here
if __name__ == '__main__':

    # Start with the empty list
    llist = LinkedList()

    # Getting the words from the File and creating a file.
    # file_name = input("\nEnter the File Name: ")
    # file_hand = open('source.txt', 'r')
    input_string = "This is Naveen, Welcome to unordered list problem"
    # FLines = input_string.readlines()
    # for line in input_string:
    words = input_string.split(' ')
    for word in words:
        llist.insert_at_end(word)
    print("\n The String is:")
    llist.display_all()

    # Searching the word in the Linked List
    Search_word = input("\nEnter the word to be searched : ")
    if llist.search(Search_word):
        llist.delete(Search_word)
        print("Word", Search_word, " found in the Linked List and deleted")
    else:
        print("Word", Search_word, " not found in the Linked List")
    # llist.display_all()

    # Updated Linked list is stored in the file a_file.txt
    # file_name = "a_file.txt"
    # file_hand = open(file_name, 'w+')
    a = llist.file_display()
    # print(a)
    input_string = a
    # file_hand.close()
    print("The Result string is: " + input_string)
    # print("File created with filename a_file.txt")
