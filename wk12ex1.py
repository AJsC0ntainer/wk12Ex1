class MobilePhone:
    
    def __init__(self, Brand, Model, StorageCapacity, Price):
        self.Brand = Brand
        self.Model = Model
        self.StorageCapacity = StorageCapacity
        self.Price = Price
        
    def DisplayPhoneDetails(self):
        print("==================================================================================================================")
        print(f"{self.Brand} phone, model {self.Model} with {self.StorageCapacity} storage capacity and a ${self.Price} pricetag.")
        print("==================================================================================================================")

phone1 = MobilePhone("Apple", "16", "2TB", "1200")
phone2 = MobilePhone("Samsung", "Galaxy S25", "1TB", "1100")

phone1.DisplayPhoneDetails()
phone2.DisplayPhoneDetails()
