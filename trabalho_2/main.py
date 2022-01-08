from threading import Thread
from time import sleep


class Node():
    def __init__(self, value = None, next = None, previous = None):
        self.value = value
        self.next = next
        self.previous = previous


class LinkedList():
    def __init__(self, head):
        self.head = head


class ReadThread(Thread):
    def __init__(self, linked_list):
        Thread.__init__(self)
        self.linked_list = linked_list

    def run(self):
        print("Thread Read, delay 3")
        sleep(self.delay)
        print(linked_list.value)
        print("Read Finished")


class InsertThread(Thread):
    def __init__(self, linked_list, value):
        Thread.__init__(self)
        self.linked_list = linked_list
        self.value = value

    def run(self):
        ll = self.linked_list.head

        while ll.next != None:
            ll = ll.next

        # Inserir na cabeça da lista
        if ll.value == None:
            ll.value = self.value
        else:
            temp = Node(value = self.value, previous=ll)
            ll.next = temp


class RemoveThread(Thread):
    def __init__(self, linked_list, value):
        Thread.__init__(self)
        self.linked_list = linked_list
        self.value = value

    def run(self):
        ll = self.linked_list.head

        while ll != None:
            if ll.value == self.value:
                break
            ll = ll.next
        
        if ll != None:
            if ll.next != None:
                ll.next.previous = ll.previous

            # caso tenho um artior conect com o próximo
            # caso não tenha um anterior, ou seja, é a cabeça, então passa a cabeça da lista pro próximo
            # caso só tenha a cabeça então cria um nó vazio
            if ll.previous != None:
                ll.previous.next = ll.next
            elif ll.next != None:
                self.linked_list.head = ll.next
            else:
                self.linked_list.head = Node()


if __name__ == '__main__':
    linked_list = LinkedList(Node())

    for i in range(0, 10):
        t = InsertThread(linked_list, i)
        t.start()
    t1 = InsertThread(linked_list, 10)
    t2 = RemoveThread(linked_list, 1)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    ll = linked_list.head

    while ll != None:
        print(ll.value)
        ll = ll.next
    
    del linked_list