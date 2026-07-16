def profile(name, country = "Canada", *skills, **details):
    print(name)
    print(country)

    if len(skills)==0:
        print("Skills:\nNone")
    else:
        for skill in skills:
            print(f"-{skill}")

    if len(details)== 0:
        print("Details:\nNone")
    else:
        for detail, value in details.items():
            print(f"{detail}:{value}")

profile("Prakash")
profile(
    "Prakash",
    "Nepal",
    "Python",
    "Git"
)

profile(
    "Prakash",
    "Nepal",
    "Python",
    "Git",
    age=24,
    university="Algoma University",
    language="English"
)