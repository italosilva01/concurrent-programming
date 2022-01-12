from threading import Thread,Lock,Condition
import os
from time import sleep

lock = Lock();
lockCond = Lock();
cond = Condition(lockCond);

class Node():
    def __init__(self, value = None, next = None, previous = None):
        self.value = value
        self.next = next
        self.previous = previous


class LinkedList():
    def __init__(self, head):
        self.head = head


class CommonThread(Thread):
    def __init__(self, linked_list, value):
        Thread.__init__(self)
        self.linked_list = linked_list
        self.value = value

def removeItem(self):
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

class ReadThread(CommonThread):
    def run(self):
        print("Buscar")
        cond.acquire()
        ll = self.linked_list.head
        cont = 0
        while ll != None:
            cont += 1
            if ll.value == self.value:
                break
            ll = ll.next

        if ll != None:
            print(f'Valor ({ll.value}) encontrado no nó {cont}!')   
       
        cond.notify()
        cond.release()
        
        
        



class InsertThread(CommonThread):
    def run(self):
        lock.acquire()
        cond.acquire()
        print('inserindo')
        ll = self.linked_list.head

        while ll.next != None:
            ll = ll.next

        # Inserir na cabeça da lista
        if ll.value == None:
            ll.value = self.value
        else:
            temp = Node(value = self.value, previous=ll)
            ll.next = temp

        lock.release()
        cond.notify()
        cond.release()


class RemoveThread(CommonThread):
    def run(self):   
          
        if(lockCond.locked()==True):
            cond.acquire()
            condition = cond.wait(10)    
      
        if lockCond.locked()==False:
            print('Removendo')           
            lock.acquire() 
            removeItem(self)
            lock.release() 

        else:
            print('Removendo')           
            if condition:
              
                removeItem(self)
            else:
                print("waiting timeout...")
            cond.release()
        


if __name__ == '__main__':
    linked_list = LinkedList(Node())

    for i in range(0, 10):
        t = InsertThread(linked_list, i)
        t.start()
    
    os.system('clear')
    
    t1 = InsertThread(linked_list, 10)
    t3 = ReadThread(linked_list, 0) 
    t4 = ReadThread(linked_list, 0)
    t5 = ReadThread(linked_list, 7)
    t2 = RemoveThread(linked_list, 1)
    t6 = RemoveThread(linked_list, 7)

  
    t3.start()
    t4.start()
    t5.start()
    t2.start()
    t1.start()
    t6.start()
    
    t1.join()
    t2.join()
    t3.join()
    t4.join()

    ll = linked_list.head

    while ll != None:
        print(ll.value)
        ll = ll.next
