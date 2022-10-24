class Organization:
 
    def __init__(self, name,address,director,phone):
        self.name = name    
        self.address = address   
        self.director = director 
        self.phone = phone 
    def __init__(self):
        pass

    def display_info(self):
        print(f"Name: {self.name}  Address: {self.address} Director: {self.director} Phone: {self.phone}")
    
    def write_info(self):
        print(f"Name: ")
        self.name = input();
        print(f"Address: ")
        self.address = input();
        print(f"Director: ")
        self.director = input();
        print(f"Phone: ")
        self.phone = input();
 
print(f"How much Organizations you want? ")
Num_of_organization = int(input());

simplelist = []


i=0
while(i<Num_of_organization):
    Company2 = Organization()
    Company2.write_info();
    Company2.display_info()
    simplelist.append(Company2)
    i=i+1

newlist = sorted(simplelist, key=lambda x: x.name, reverse=False)

for obj in newlist:
    print(f"Name: {obj.name}  Address: {obj.address} Director: {obj.director} Phone: {obj.phone}")