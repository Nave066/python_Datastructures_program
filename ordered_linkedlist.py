# @node class for
class Node:
    # @ constructor
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    # @ for getting data
    def getData(self):
        return self.data

    # @ for setting data
    def getNext(self):
        return self.next

    # @ for getting data
    def setData(self, newdata):
        self.data = newdata

    # @ for setting data
    def setNext(self, newnext):
        self.next = newnext


# @ ordered list class for link list
class OrderedList:
    # @constructor
    def __init__(self):
        self.head = None

    # @ for search data item
    def search(self, item):
        current = self.head
        found = False
        stop = False

        while current is not None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    # @ for adding data
    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def print(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


if __name__ == "__main__":
    ordered_list = OrderedList()
    input_list = [5, 7, 9, 1, 8, 1]
    for i in input_list:
        ordered_list.add(i)
    search_input = int(input("Enter the number to search"))
    print(ordered_list.search(search_input))
    print(ordered_list.print())
