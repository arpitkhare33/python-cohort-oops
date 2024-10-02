# ===================================== Object oriented programming systems ------------------------------------------

# 1. What is OOPS -- done
# 2. Need of OOPS -- done
# 3. Create a Class -- done
# 4. Create Object -- done
# 5. Init Function -- done
# 6. __str__ function  -- done
# 7. Object Methods -- done
# 8. Self Parameter -- done
# 9. Modify Existing Object Properties -- done
# 10. Deleting Object Properties and Whole Objects -- done

# ==================================== Python Level 2: OOPS ==========================================================



# 1 BHK => 1 Hall, 1 Bed Room, 1 Kitchen=> Class
# 1 bhk => 1 Hall (200 sqft), 1 Bed Room( 100 sqft),  1 Kitchen( 40 sqft ) => Object


#
# class Person:  # MAP
#     name = "Arpit"
#
#
# p1 = Person()  # A HOUSE
# print(p1.name)



class Person:
    def __init__(self, name, age, city): # Constructor
        self.name = name
        self.age = age
        self.city = city

    def __str__(self):
        return f"{self.name}, {self.age}, {self.city}"

    def introduce(self):
        print("My name is: ", self.name)
        print("My age is: ", self.age)
        print("My city is: ", self.city)


p1 = Person("Rohan Sharma", 26, "Mumbai")
p2 = Person("Amit Yadav", 27, "Delhi")
p3 = Person("Neha", 25, "Bangalore")
p4 = Person("Anushka Sharma", 29, "Hyderabad")
# p1.introduce()
# p2.introduce()
# p3.introduce()
p4.introduce()

p4.age = 39
p4.introduce()

del p4
p4.introduce()




























