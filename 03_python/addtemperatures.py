T_0 = float(input("Please enter the starting temperature in degrees Kelvin: "))

d_theta = float(input("Please enter the changing of temperature in degrees Fahrenheit: "))

dT = (5/9)*(d_theta - 32) + 273.15

T =  T_0 + dT

print("The new temperature is", T, "degrees Kelvin.  Have a nice day.")
