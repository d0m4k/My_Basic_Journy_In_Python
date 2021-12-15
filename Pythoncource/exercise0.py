weight_in_pounds = input("Enter your weight in pounds: ")
def pounds_kilo(pound, kilo):
    return pound*kilo
result = pounds_kilo(float(weight_in_pounds), 0.45359237)
print(f"The kilogram of {weight_in_pounds} pounds is {result} kilograms.")
