#Custom class for mobile phone
class MobilePhone:
    #Mobile phone constructor
    def __init__(self, Brand, Model, StorageCapacity, Price):
        #Constructor properties
        self.Brand = Brand
        self.Model = Model
        self.StorageCapacity = StorageCapacity
        self.Price = Price
    #Method to display details
    def DisplayPhoneDetails(self):
        #Styling
        print("==================================================================================================================")
        #Print Phone details
        print(f"{self.Brand} phone, model {self.Model} with {self.StorageCapacity} storage capacity and a ${self.Price} pricetag.")
        #Styling
        print("==================================================================================================================")
#Phone object 1
phone1 = MobilePhone("Apple", "16", "2TB", "1200")
#phone object 2
phone2 = MobilePhone("Samsung", "Galaxy S25", "1TB", "1100")

#Call to method to display object 1 details
phone1.DisplayPhoneDetails()
#Call to method to display object 1 details
phone2.DisplayPhoneDetails()

#Pushed to GitHub wk12ex1 repo.