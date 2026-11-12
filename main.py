git init
from profile import StudentProfile
from playlist import display_playlist

student = StudentProfile(
    name="Aaron James ",
    age="14",
    favorite="Sports",
    hobbies=["roblox", "Sports", "Tiktok"]
)

student.display_profile()
display_playlist()
