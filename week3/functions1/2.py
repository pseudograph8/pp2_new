'''
2.Read in a Fahrenheit temperature. 
Calculate and display the equivalent centigrade temperature. 
The following formula is used for the conversion: C = (5 / 9) * (F - 32)
'''
def temp(far):
    centigrade = (5/9)*(far - 32)
    print(f"centigrade = {centigrade}")

initial = float(input("Enter a Fahrenheit temperature: "))
temp(initial)