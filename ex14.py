from sys import argv

script, user_name = argv

prompt = '>'

print(f"Hi {user_name}, I'm the {script} script ")

print("I'd like to ask you a few questions.")

print(f"Do you like me {user_name}")
likes = input(prompt)

print("Where do you live")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about me.
And you live in {lives}. Not sure where that it is.
And you have a {computer} computer. Nice. """)
