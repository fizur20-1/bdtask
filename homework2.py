# class Vehicle:
#   def __init__(self, VehicleName,Speed,Mileage):
#     self.VehicleName = VehicleName
#     self.Speed = Speed
#     self.Mileage=Mileage

#   def printInfo(self):
#     print("","Vehicle Name:",self.VehicleName, "\n","Speed:",
#           self.Speed,"\n","Mileage:",self.Mileage )

# class Bus(Vehicle):
#   pass

# x1 = Bus("school volvo", 180, 12)
# x1.printInfo()

# another approach : 

# class Vehicle:
#     def __init__(self, name, speed, mileage):
#         self.name = name
#         self.speed = speed
#         self.mileage = mileage

#     def display_info(self):
#         print("Vehicle Name:", self.name)
#         print("Speed:", self.speed)
#         print("Mileage:", self.mileage)


# class Bus(Vehicle):
#     def __init__(self, name, speed, mileage, capacity):
#         super().__init__(name, speed, mileage)
#         self.capacity = capacity

#     def display_capacity(self):
#         print("Capacity:", self.capacity)


# bus = Bus("School Volvo", 180, 12, 50)
# bus.display_info()
# bus.display_capacity()

# 2nd ques:

# class Vehicle:
#   def __init__(self, VehicleName,Speed,Mileage):
#     self.VehicleName = VehicleName
#     self.Speed = Speed
#     self.Mileage=Mileage

#   def printInfo(self):
#     print("","Vehicle Name:",self.VehicleName, "\n","Speed:",
#           self.Speed,"\n","Mileage:",self.Mileage )

# class Bus(Vehicle):
#   def __init__(self, VehicleName,Speed,Mileage,TotalSeat):
#      super().__init__(VehicleName, Speed, Mileage)
#      self.TotalSeat=TotalSeat
    
#   def display_capacity(self):
      
#       print("","Capacity:", self.TotalSeat)  

#       fare=self.TotalSeat*100
#       MaintenanceCharge = fare * 0.1
#       TotalFare = fare + MaintenanceCharge
#       print("","Total fare:",TotalFare)

# bus = Bus("School Volvo", 180, 12, 50)
# bus.printInfo()
# bus.display_capacity()
