git init
from profile import StudentProfile
from playlist import display_playlist

student = StudentProfile(
    name="Not provided",
    age="Not provided",
    favorite="Not provided",
    hobbies=["Hobby 1", "Hobby 2", "Hobby 3"]
)

student.display_profile()
display_playlist()