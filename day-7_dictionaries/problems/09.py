"""Create a dictionary called laptop with:
"brand" → "Apple"
"model" → "MacBook Air"
"year" → 2025

Then perform these operations in order:
Update "year" to 2026.
Add a new key "color" with value "Midnight".
Print the value of "model" using direct access ([]).
Print the value of "storage" using .get().
Print the value of "storage" again using .get() with the default value "256GB".
Remove "color" using .pop() and store the removed value in a variable.
Print the final dictionary.
Print the removed color."""

laptop = {
    "brand": "Apple",
    "model": "MacBook Air",
    "year": 2025
}
laptop["year"]= 2026
laptop["color"]= "Midnight"
print(laptop["model"])
print(laptop.get("storage"))
print(laptop.get("storage", "256GB"))
removed = laptop.pop("color")
print(laptop)
print(removed)