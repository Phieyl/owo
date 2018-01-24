import time
def countdown(n) :
    while n > 0:
        print (n)
        n = n - 1
        if n ==0:
            print('Gridcoin')
        time.sleep(1)
countdown(int(input('Insert your essance ')))
