git init
class StudentProfile:
    def __init__(self, name, age, favorite, hobbies):
        self.name = name
        self.age = age
        self.favorite = favorite
        self.hobbies = hobbies

    def display_profile(self):
        print("===== STUDENT PROFILE =====")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Favorite:", self.favorite)
        print("Hobbies:", ", ".join(self.hobbies))

git config --local user.name "Riley Loves Cock"
git config --local user.email "supergawk3000@gmail.com"