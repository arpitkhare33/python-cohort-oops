# ================================ Inheritance in Python ===================================================

# 1. Inheritance Basics -- Done
# 2. Need of Inheritance -- Done
# 3. Create a Parent Class -- Done
# 4. Create a Child Class -- Done
# BONUS: Method Overriding -- Done
# 5. Adding __init__ function -- Done
# 6. Using the super() function -- Done
# 7. Add Properties in Child Class -- Done
# 8. Add Methods in Child Class

# ==========================================================================================================


# ================================ Inheritance in Python =====================================================

# Person: Name, Adhar card, Mob, BookId

# Teacher: Name, Adhar card, Mob, BookId
# Student: Name, Adhar card, Mob, BookId, EnrollNum, RollNo., Semester, Course
# Vendor: Shop name, ......, Name, Adhar card, BookId
# Librarian

# Student: Inherit Person, EnrollNum, RollNo, Semester, Course
# =========================================================================================

# Creating a parent class
class Person:
    def __init__(self, name, adhar, mob, book_id): # Raman", "8765431010", 987654310, "BOOK123456"
        self.name = name
        self.adhar = adhar
        self.mob = mob
        self.book_id = book_id

    def intro(self):
        print("My name is ", self.name)
        print("My adhar is ", self.adhar)
        print("My mobile no. is ", self.mob)
        print("I have taken the book with book id: ", self.book_id)


# Create a child class
class Student(Person):
    def __init__(self, name, adhar, mob, book_id, e_num, r_no, sem, course):
        super().__init__(name, adhar, mob, book_id)
        self.e_num = e_num
        self.r_no = r_no
        self.sem = sem
        self.course = course

    def intro(self):
        super().intro()
        print("My name is ", self.name)
        print("My Enrollment ID is ", self.e_num)
        print("My Roll No is ", self.r_no)
        print("My sem is ", self.sem)
        print("My course is ", self.course)

    def give_exam(self):
        print(f"Student {self.name} is giving the exam of {self.course}. He studied from the book {self.book_id}")


s1 = Student("Raman", "8765431010", 987654310, "BOOK123456", "E123", "R1", "Sem 1", "Python")
# s1.intro()
s1.give_exam()

# which_mobile_phone => nokia 3315
# which_mobile_phone => nokia 2730

p1 = Person("Raghav", "21243434", 34523145, "BOOK9876")
p1.give_exam()



# Parent to Child => Inheritance
# Child to Parent => Not possible
