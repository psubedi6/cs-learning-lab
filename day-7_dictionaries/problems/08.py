"""Create a dictionary called school with the following structure:
"name" → "Algoma University"
"location" → another dictionary containing:
"city" → "Brampton"
"province" → "Ontario"
"country" → "Canada"

Then print only:
the entire "location" dictionary
the "city"
the "country"""


school = {
    "name" : "Algoma University",
    "location": {
        "city" : "Brampton",
        "province" : "Ontario",
        "country": "Canada"
    }
}
print(school["location"])
print(school["location"]["city"])
print(school["location"]["country"])