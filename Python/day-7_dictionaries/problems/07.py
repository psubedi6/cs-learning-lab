"""Create a dictionary called employee with:
"name" → "John"
"department" → "IT"
"salary" → 60000

Then:
Print the value of "name" using direct access ([]).
Print the value of "department" using .get().
Print the value of "email" using .get().
Print the value of "email" again using .get() with a default value "Email not available".
Do not use square brackets for "email"."""

employee={
    "name": "John",
    "department": "IT",
    "salary" : 60000
}
print(employee["name"])
print(employee.get("department"))
print(employee.get("email"))
print(employee.get("email","Email not available"))