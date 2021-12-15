birth_year = int(input("Enter your Birth_Year: "))
current_year = int(input("Enter Current year: "))
def age(b_year, c_year):
    return c_year - b_year
my_age = age(birth_year, current_year)
print(f"Your age is {my_age}")
    
