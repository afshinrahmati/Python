maxLive = 90
age = int(input("what is your age?"))

finalAge = maxLive - age

day = 365 * finalAge
month = 12 * finalAge
week = 52 * finalAge

print("day:" , day ,"\n month" , month ,"\n week" , week)