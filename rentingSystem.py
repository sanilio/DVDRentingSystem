"""
Author: Sanil Sampat
Date:   10 / 28 / 12
Usage: 

        $ python rentingSystem.py
"""

from datetime import date
from datetime import timedelta 

class DVD:

    def __init__(self, title, genre, upc, copies=1, status=True):

            self.title       = title
            self.genre       = genre
            self.upc         = upc
            self.copies      = copies  
            self.status      = status
            self.renters     = []

    def addCopy(self):

            self.copies      += 1
            self.status       = True

    def removeCopy(self):

            self.copies -= 1

            if self.copies == 0:
                    self.status = False

    def printRenters(self):
            
            print "Renters for %s:" % self.title

            for (renter, date) in self.renters:
                    print "Renter: %s, Due: %s" % (renter.name, date)
    
    def removeRenter(self, customer):

            for i, (renter, date) in enumerate(self.renters):
                    if renter == customer:
                            del self.renters[i]

class Customer:

    def __init__(self, name, phone, address, state, zip):

            self.name       = name
            self.phone      = phone
            self.address    = address
            self.state      = state
            self.zip        = zip
            self.rentedDVDs = []

    def addRentedDVD(self, dvd):
            
            returnDate = date.today() + timedelta(days=3)

            self.rentedDVDs.append((dvd, returnDate))

    def removeRentedDVD(self, returnDVD):

            for i, (dvd, date) in enumerate(self.rentedDVDs):
                    if dvd == returnDVD:
                            del self.rentedDVDs[i]

    def printRentedDVDs(self):

            for (dvd,  date) in self.rentedDVDs:
                    print "%s, %s is due %s." % (self.name, dvd.title, date)

inventory = {} 
customers = []


def addCustomer(customer):

        customers.append(customer)

def addDVD(dvd):
        
        if inventory.has_key(dvd.upc):

                inventory[dvd.upc].addCopy()

        else:
                inventory[dvd.upc] = dvd 

def rentDVDToCustomer(dvd, customer):

        if inventory.has_key(dvd.upc) and inventory[dvd.upc].status == True:

                customer.addRentedDVD(dvd)
                
                inventory[dvd.upc].renters.append((customer, date.today() + timedelta(days=3)))

                inventory[dvd.upc].removeCopy()

                print "%s, thank you for renting %s from us! Enjoy!" % (customer.name, dvd.title)
        
        else:   print "Sorry %s, %s is not available." % (customer.name, dvd.title)



def returnDVD(dvd, customer):

        customer.removeRentedDVD(dvd)

        dvd.removeRenter(customer)

        inventory[dvd.upc].addCopy()

        print "%s, thank you for returning %s, we hope you liked it!" % (customer.name, dvd.title)



# create some dvds and add them to the inventory
dvd0 = DVD("Lord of the Rings",        "Epic",      01, 3)
dvd1 = DVD("Pirates of the Caribbean", "Adventure", 02, 1)
dvd2 = DVD("Harry Potter",             "Family",    03, 1)

addDVD(dvd0)
addDVD(dvd1)
addDVD(dvd2)

# create some customers and add them to the customer list
cust0 = Customer("Sanil", 8157917670, "1151 W 14th Pl", "IL", 60608)
cust1 = Customer("Nicky", 8157396580, "2240 N Lasalle", "IL", 60612)
cust2 = Customer("Rahul", 8157396576, "9665 S 22nd St", "IL", 60348)
cust3 = Customer("Peter", 8157292663, "5354 E Ruby Dr", "IL", 60435)

addCustomer(cust0)
addCustomer(cust1)
addCustomer(cust2)
addCustomer(cust3)


# a test sequence of renting, returning, and displaying return dates
rentDVDToCustomer(dvd0, cust0)
rentDVDToCustomer(dvd0, cust1)
rentDVDToCustomer(dvd0, cust2)
rentDVDToCustomer(dvd0, cust3)

cust0.printRentedDVDs()

returnDVD(dvd0, cust0)

rentDVDToCustomer(dvd0, cust3)

cust3.printRentedDVDs()

rentDVDToCustomer(dvd1, cust1)

rentDVDToCustomer(dvd2, cust1)

cust1.printRentedDVDs()

rentDVDToCustomer(dvd1, cust2)

returnDVD(dvd1, cust1)

rentDVDToCustomer(dvd1, cust2)

cust2.printRentedDVDs()

dvd0.printRenters()
