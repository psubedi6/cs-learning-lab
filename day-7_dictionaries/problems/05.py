"""Create a dictionary called user with:
"username" → "prakash123"
"email" → "prakash@gmail.com"
"country" → "Canada"
"language" → "English"

Then do both of these:
remove "country" using del
remove "language" using .pop()

After that:
print the final dictionary
print the value that was removed by .pop()"""

user= {
    "username": "prakash123",
    "email": "prakash@gmail.com",
    "country": "Canada",
    "language": "English"

}
del user["country"]
a = user.pop("language")
print(user)
print(a)