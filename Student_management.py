class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_details(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)

    def update_marks(self, new_marks):
        self.marks = new_marks
        print("Marks updated successfully!")

    def get_result(self):
        if self.marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")


# Main Program
student1 = Student("Amey", 101, 78)

student1.display_details()
student1.get_result()

student1.update_marks(35)
student1.get_result()
