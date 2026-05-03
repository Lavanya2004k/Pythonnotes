# class myname:
#     f_name="Lavhanya"
#     l_name="Kotha"
# print(myname)

# class myname:
#    f_name="Lavhanya"
#    l_name="Kotha"
# your_name=myname() # created object based on class and utilized it 
# #del your_name
# print(your_name.f_name)
# print(your_name.l_name)
# pass

# class Employee:
#     n_emps=0
#     raise_amount1=1.04 # class variables --- class variables are used among the all instances
#     def __init__(self,first,second,pay):  #these self variables are instances as they are only created with restrictions to these functions
#         self.first=first
#         self.second=second
#         self.pay=pay
#         Employee.n_emps+=1
#     def fullname(self):
#         return '{}{}'.format(self.first,self.second)
#     def apply_raise(self):
#         self.pay = int(self.pay * Employee.raise_amount1)
#     @classmethod
#     def set_raiseamount(cls,amount): #cls is variable that is being used in this class ---- In class method cls is like self that we use in normal class
#         cls.new_raise=amount
        
# emp1 = Employee("Lavhanya","Kotha",5000) # they are called objects/instances because they are using class
# emp2 = Employee("N",3000)
# Employee.set_raiseamount(1.05)
# print(Employee.n_emps)
# print(emp1.fullname())
# emp1.apply_raise()
# print(emp1.pay)
# print(Employee.new_raise)





