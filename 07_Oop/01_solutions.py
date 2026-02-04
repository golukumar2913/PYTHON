"""Class And Obj"""

# class Car:
#    def __init__(self, brand, model):
#       self.brand = brand
#       self.model = model


#    def full_name(self):
#       return f"{self.brand} {self.model}"



# my_car = Car("Toyata", "Corolla")    
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())



# my_new_car = Car("TATA", "Safari")
# print(my_new_car.model) 




"""inhertance"""

# class Car:
#    def __init__(self, brand, model):
#       self.brand = brand
#       self.model = model


#    def full_name(self):
#       return f"{self.brand} {self.model}"
   

# class ElectricCar(Car):
#    def __init__(self, brand, model, battery_size):
#       super().__init__(brand, model)
#       self.battery_size = battery_size



# my_tesla = ElectricCar("Tesla", "Model S", "85kWh") 
# print(my_tesla.model)  
# print(my_tesla.full_name()) 



"""Encapsulation"""

# class Car:
#    def __init__(self, brand, model):
#       self.__brand = brand
#       self.model = model

#    def get_barnd(self) :
#       return self.__brand + "!" 


#    def full_name(self):
#       return f"{self.__brand} {self.model}"
   

# class ElectricCar(Car):
#    def __init__(self, brand, model, battery_size):
#       super().__init__(brand, model)
#       self.battery_size = battery_size



# my_tesla = ElectricCar("Tesla", "Model S", "85kWh") 
# # print(my_tesla.__brand)  
# print(my_tesla.get_barnd())
# print(my_tesla.full_name()) 



"""Polymorphism"""


# class Car:
#    def __init__(self, brand, model):
#       self.__brand = brand
#       self.model = model

#    def get_barnd(self) :
#       return self.__brand + "!" 


#    def full_name(self):
#       return f"{self.__brand} {self.model}"
   
#    def fuel_type(self):
#       return "Petrol or Disel"
   

# class ElectricCar(Car):
#    def __init__(self, brand, model, battery_size):
#       super().__init__(brand, model)
#       self.battery_size = battery_size

#    def fuel_type(self):
#       return "Electric Charge"   



# my_tesla = ElectricCar("Tesla", "Model S", "85kWh") 

# print(my_tesla.fuel_type())

# my_safari = Car("Tata", "Safari")
# print(my_safari.fuel_type())



"""Count Car Created"""

# class Car:
#    total_car = 0

#    def __init__(self, brand, model):
#       self.__brand = brand
#       self.model = model
#       Car.total_car += 1

#    def get_barnd(self) :
#       return self.__brand + "!" 


#    def full_name(self):
#       return f"{self.__brand} {self.model}"
   
#    def fuel_type(self):
#       return "Petrol or Disel"
   

# class ElectricCar(Car):
#    def __init__(self, brand, model, battery_size):
#       super().__init__(brand, model)
#       self.battery_size = battery_size

#    def fuel_type(self):
#       return "Electric Charge"   



# my_tesla = ElectricCar("Tesla", "Model S", "85kWh") 
# print(my_tesla.full_name())

# my_safari = Car("Tata", "Safari")
# print(my_safari.fuel_type())

# my_nexon = Car("Tata", "Nexon")
# print(my_nexon.full_name())

# print(Car.total_car)
# print(Car.total_car)
# print(Car.total_car)

"""Static Method"""
# class Car:
#    total_car = 0

#    def __init__(self, brand, model):
#       self.__brand = brand
#       self.model = model
#       Car.total_car += 1

#    def get_barnd(self) :
#       return self.__brand + "!" 


#    def full_name(self):
#       return f"{self.__brand} {self.model}"
   
#    def fuel_type(self):
#       return "Petrol or Disel"
   
#    @staticmethod
#    def car_descri():
#       return "Car is best in transport"
   

# class ElectricCar(Car):
#    def __init__(self, brand, model, battery_size):
#       super().__init__(brand, model)
#       self.battery_size = battery_size

#    def fuel_type(self):
#       return "Electric Charge"   



# my_tesla = ElectricCar("Tesla", "Model S", "85kWh") 
# print(my_tesla.full_name())

# my_safari = Car("Tata", "Safari")
# print(my_safari.fuel_type())

# my_nexon = Car("Tata", "Nexon")
# print(my_nexon.full_name())

# print(Car.total_car)

# print(Car.car_descri())


"""Property Decorater"""

# class Car:
#    total_car = 0

#    def __init__(self, brand, model):
#       self.__brand = brand
#       self.__model = model
#       Car.total_car += 1

#    def get_barnd(self) :
#       return self.__brand + "!" 


#    def full_name(self):
#       return f"{self.__brand} {self.__model}"
   
#    def fuel_type(self):
#       return "Petrol or Disel"
   
#    @staticmethod
#    def car_descri():
#       return "Car is best in transport"
   
#    @property
#    def model(self):
#       return self.__model
   

# class ElectricCar(Car):
#    def __init__(self, brand, model, battery_size):
#       super().__init__(brand, model)
#       self.battery_size = battery_size

#    def fuel_type(self):
#       return "Electric Charge"   



# my_tesla = ElectricCar("Tesla", "Model S", "85kWh") 
# print(my_tesla.full_name())

# my_safari = Car("Tata", "Safari")
# # my_safari.model = "City"

# print(Car.total_car)

# print(Car.car_descri())

# print(my_safari.model)


"""Check Instance"""

# class Car:
#    total_car = 0

#    def __init__(self, brand, model):
#       self.__brand = brand
#       self.__model = model
#       Car.total_car += 1

#    def get_barnd(self) :
#       return self.__brand + "!" 


#    def full_name(self):
#       return f"{self.__brand} {self.__model}"
   
#    def fuel_type(self):
#       return "Petrol or Disel"
   
#    @staticmethod
#    def car_descri():
#       return "Car is best in transport"
   
#    @property
#    def model(self):
#       return self.__model
   

# class ElectricCar(Car):
#    def __init__(self, brand, model, battery_size):
#       super().__init__(brand, model)
#       self.battery_size = battery_size

#    def fuel_type(self):
#       return "Electric Charge"   



# my_tesla = ElectricCar("Tesla", "Model S", "85kWh") 
# print(my_tesla.full_name())

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))


"""Multiple Inheritance"""

class Car:
   total_car = 0

   def __init__(self, brand, model):
      self.__brand = brand
      self.__model = model
      Car.total_car += 1

   def get_barnd(self) :
      return self.__brand + "!" 


   def full_name(self):
      return f"{self.__brand} {self.__model}"
   
   def fuel_type(self):
      return "Petrol or Disel"
   
   @staticmethod
   def car_descri():
      return "Car is best in transport"
   
   @property
   def model(self):
      return self.__model

class Battery:
   def battery_info(self):
      return "This is battery"

class Engine:
   def engine_info(self):
      return "This is engine"     


class ElectricCarTwo(Battery, Engine, Car):
   pass


my_new_tesla = ElectricCarTwo("Tesla", "model Y")

print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())
