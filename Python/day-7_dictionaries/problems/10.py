"""Create a dictionary called person with:
"name" → "Prakash"
"age" → 24
"address" → another dictionary containing:
"city" → "Toronto"
"province" → "Ontario"

Then perform these operations in order:
Print the person's name.---
Print the city from the nested dictionary.---
Update the age to 25.---
Add a new key "country" with value "Canada".---
Print all the keys using .keys().---
Print all the values using .values().---
Print all the key-value pairs using .items().---
Print the value of "email" using .get() with the default value "No email found".---
Remove "country" using .pop() and store it in a variable.
Print the final dictionary.
Print the removed country."""

person = {
    "name": "Prakash",
    "age": 24,
    "address":{
        "city": "Toronto",
        "province":  "Ontario"
    }
}
print(person["name"])
print(person["address"]["city"])
person["age"] = 25
person["country"] = "Canada"
print(person.keys())
print(person.values())
print(person.items())
print(person.get("email", "No email found"))
restored = person.pop("country")
print(person)
print(restored)