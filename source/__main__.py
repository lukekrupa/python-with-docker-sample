import sys 

from lib import Customer

def run_project(args):
    customer = Customer('Joe Doe', 1000.0)
    customer.withdraw(500.0)
    print('Balance: %.2f' % (customer.balance))

if __name__ == '__main__':
    run_project(sys.argv)
