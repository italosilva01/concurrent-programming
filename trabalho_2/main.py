from threading import Thread,Lock,Condition
import os
from time import sleep

lock = Lock()
lockCond = Lock()
cond = Condition(lockCond)

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

        # inserir na cabeça da lista, caso ainda não tenha nenhum nó com valor inserido
        if ll.value == None:
            ll.value = self.value
        else:
            temp = Node(value = self.value, previous=ll)
            ll.next = temp

        lock.release()
        cond.notify()
        cond.release()


class RemoveThread(CommonThread):
    def removeItem(self):
        ll = self.linked_list.head
        while ll != None:
            if ll.value == self.value:
                # casjo seja a cabeça
                if ll.previous == None:
                    # caso só tenha a cabeça, e precise removê-la
                    if ll.next == None:
                        self.linked_list.head = Node()
                    else: 
                        # caso tenha um próximo, 
                        # o próximo se tornará a cabeça
                        self.linked_list.head = ll.next
                else:
                    # caso seja o último da lista, o next do anterior deve ser nulo
                    if ll.next == None:
                        ll.previous.next = None
                    else:
                        # caso tenha um previous e um next, conecta os dois
                        ll.previous.next = ll.next
                        ll.next.previous = ll.previous

                # removendo o nó da memória
                del ll
                # encerrando a removação
                break
            ll = ll.next

    def run(self):   
        if(lockCond.locked() == True):
            cond.acquire()
            condition = cond.wait(5)    

        if lockCond.locked() == False:
            print('Removendo')           
            lock.acquire() 
            self.removeItem()
            lock.release() 
        else:
            print('Removendo')           
            if condition:
                self.removeItem()
            else:
                print("waiting timeout...")
            cond.notify()
            cond.release()


if __name__ == '__main__':
    # Criando a lista
    linked_list = LinkedList(Node())

    # inserindo 10 números na lista
    for i in range(0, 10):
        t = InsertThread(linked_list, i)
        t.start()

    os.system('clear')

    t1 = InsertThread(linked_list, 10)
    t3 = ReadThread(linked_list, 0) 
    t4 = ReadThread(linked_list, 1)
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
    t5.join() 
    t6.join()

    ll = linked_list.head

    while ll != None:
        print(ll.value)
        ll = ll.next
