import random

subjects = [
    "Physics Professor",
    "Sleep-Deprived Coder",
    "Confused Historian",
    "Overconfident Hacker",
    "Emotional AI",
    "Procrastinating Student",
    "Grammar Police Officer",
    "Forgotten Scientist",
    "Bug-Hunting Intern",
    "Space Tourist",
    "WiFi-Seeking Nomad",
    "Math Wizard"
]


actions = [
    "arguing with a toaster",
    "debugging life decisions",
    "accidentally launching a rocket",
    "googling how to google",
    "writing code that writes breakup letters",
    "trying to divide by zero",
    "hacking a vending machine",
    "thinking WiFi is a human right",
    "mistaking shampoo for chemistry experiment",
    "overclocking their brain",
    "explaining memes in binary",
    "escaping from a group project"
]

places = [
    "in the middle of a Zoom call",
    "inside the campus dustbin WiFi zone",
    "on Mars (but with lag)",
    "in the bathroom labeled ‘404’",
    "under the desk during a fire drill",
    "in the Forbidden Folder",
    "inside a PowerPoint presentation",
    "on the dark web cooking show",
    "in the principal’s office... again",
    "on a Windows XP loading screen",
    "inside ChatGPT’s imagination",
    "at the ‘No Signal’ mountain peak"
]

laughing_emojis = [
    "😂", "🤣", "😆", "😹", "😄", "😜", "🤪", "🙃", "😹😂", "😂💀", "🤣🔥"
]




while True:
    subject = random.choice(subjects)
    act = random.choice(actions)
    place = random.choice(places)
    emoji = random.choice(laughing_emojis)

    print(f"{subject} {act} {place} {emoji}")

    user_input = input("Press 'c' to generate another news item or type 'exit' to quit: ")
    if user_input.lower() == 'c':
        continue
    elif user_input.lower() == 'exit':
        print("Exiting the news generator.")
        break
    else:
        print("Invalid input. Please type 'e' to continue or 'exit' to quit.")
        break