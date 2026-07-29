#integer
age = 25
score = -10
big_score = 1_000_000
print(age)
print(score)
print(big_score)
print(type(age))


#float
price= 9.99
temperatre = -3.5
science = 1.5e4
print(price)
print(temperatre)
print(science)
print(type(price))


#string
name= "Prakash"
greeting = "Hello World"
multi = """This is
a multi-line 
string"""
number_as_string = "42"
print(name)
print(greeting)
print(multi)
print(number_as_string)
print(type(name))
print(type(number_as_string))


#boolean and none
is_logged_in = True
has_paid = False
print(is_logged_in)
print(has_paid)
print(type(is_logged_in))
# --- NONE ---
result = None
user = None
print(result)
print(type(result))


#Type() vs isinstance()
age = 25
name= "Prakash"
is_logged_in = True
#type()
print(type(age))
print(type(name))
print(type(is_logged_in))
#isinstance()
print(isinstance(age, int))
print(isinstance(name, str))
print(isinstance(is_logged_in, bool))
# the interesting one
print(isinstance(True, int))



# --- BOOL IS SECRETLY INT ---
print(True + True)
print(True + False)
print(False + False)
print(True * 10)
print(True == 1)
print(False == 0)



# --- TYPE COERCION ---
# Converting to int
print(int("42"))
print(int(3.9))
print(int(True))
print(int(False))
# Converting to float
print(float("3.14"))
print(float(42))
# Converting to string
print(str(100))
print(str(3.14))
print(str(True))
# Converting to bool
print(bool(1))
print(bool(0))
print(bool("hello"))
print(bool(""))
print(bool(None))


# --- MUTABILITY VS IMMUTABILITY ---
# Strings are immutable
name = "Prakash"
print(id(name))
name = "Prakash Subedi"
print(id(name))
# Watch the id change - proof a new object was created
# Int is immutable too
x = 10
print(id(x))
x = 20
print(id(x))


# --- IMMUTABILITY PROOF ---
a = "hello"
b = a
print("before:", a, b)
print("id a:", id(a))
print("id b:", id(b))
a = "world"
print("after:", a, b)
print("id a:", id(a))
print("id b:", id(b))

# --- INTERVIEW PREP ---
# == vs is
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)    # compares VALUES
print(a is b)    # compares MEMORY ADDRESS
# None check
print(a == None)
print(a is None)
# The correct way to check for None
result = None
print(result is None)

# --- NONE vs FALSE vs 0 ---
print(None == False)
print(None == 0)
print(False == 0)
print(None is False)
print(None is 0)
print(bool(None))
print(bool(False))
print(bool(0))
print(type(None))
print(type(False))
print(type(0))