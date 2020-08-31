import threading
import time
import random


# def execute_thread(i):
#     #time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) #ładnie sformatowany czas
#     print("Thread {} sleeps at {}".format(i, time.strftime("%H:%M:%S", time.gmtime())))
#
#     rand_sleep_time = random.randint(1,4)
#     time.sleep(rand_sleep_time)
#     print("Thread {} stops sleeping at {}".format(i, time.strftime("%H:%M:%S", time.gmtime())))
#
# for i in range(10):
#     thread = threading.Thread(target=execute_thread, args=(i,)) # args must be a sequence
#     thread.start()
#
#     print("Active Threads: ", threading.activeCount())
#     print("Thread objects: ", threading.enumerate())


###############################
# subclass thread
class CustomThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        get_time(self.name)
        print("Thread", self.name, "Execution Ends")

def get_time(name):
    print("Thread {} sleeps at {}".format(name, time.strftime("%H:%M:%S", time.gmtime())))
    rand_sleep_time = random.randint(1,4)
    time.sleep(rand_sleep_time)


thread1 = CustomThread("1")
thread2 = CustomThread("2")

thread1.start() # tak naprawde uruchamia metode run
thread2.start()

print("Thread 1 Alive: ", thread1.is_alive())
print("Thread 2 Alive: ", thread2.is_alive())

print("Thread 1 name: ", thread1.getName())
print("Thread 2 name: ", thread2.setName("nowe imie"))
print("Thread 2 name: ", thread2.getName())

thread1.join() #czeka na exit innych watkow
thread2.join()

print("Execution ends")


###################################
# synchronizing threads
class BankAccount(threading.Thread):
    acct_balance = 100
    def __init__(self, name, money_request):
        threading.Thread.__init__(self)
        self.name = name
        self.money_request = money_request

    def run(self):
        # uruchamiana przez obiekt_thread.start()
        thread_lock.acquire()
        BankAccount.get_money(self)
        thread_lock.release()

    @staticmethod
    def get_money(customer): #obiekt klasy BankAccount ze swoimi atrybutami
        print("{} tries to withdraw ${} at {}".format(customer.name, customer.money_request,
                                                      time.strftime("%H:%M:%S", time.gmtime())))
        if BankAccount.acct_balance - customer.money_request > 0:
            BankAccount.acct_balance -= customer.money_request
            print("New Account Balance is : ${}".format(BankAccount.acct_balance))
        else:
            print("Not Enough Money in Account")
            print("Current Balance is: ${}".format(BankAccount.acct_balance))
            time.sleep(3)


thread_lock = threading.Lock()
doug = BankAccount("Doug", 1)
paul = BankAccount("Paul", 100)
sally = BankAccount("Sally", 50)

doug.start()
paul.start()
sally.start()

#synchronizacja, czekają na siebie
doug.join()
paul.join()
sally.join()