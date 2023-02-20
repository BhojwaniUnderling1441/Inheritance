class Person:
    def __init__(self,name,address,phone):
        self.name = name
        self.address = address
        self.phone = phone

    def print_person(self):
        print (self.name,self.address,self.phone)

class Customer(Person):
    def __init__(self,name,address,phone,customerid,mail):
        Person.__init__(self,name,address,phone)

        self.customerid = customerid
        self.mail = mail
    
    def print_customer(self):
        print (self.name,self.address,self.phone,self.customerid,self.mail)


customer = Customer('Todd','Todds House','555-555-5555',141,True)
customer.print_customer()