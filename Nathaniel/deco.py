




class Employe:

    def __init__(self , name , lastname):
        self.name=name
        self.lastname= lastname


    def __str__(self):
        return 'his name his {} , {}' .format(self.name,self.lastname)



    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.name , self.lastname)


    def fullname(self):
        return '{} {}'.format(self.name , self.lastname)





emp_1= Employe('george', 'smith')

print(emp_1.fullname())
print(emp_1.email)
print(emp_1.lastname)