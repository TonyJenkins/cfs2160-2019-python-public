#Python 3.4
import statistics as sp
temperatures = []
temperatures.append(float(input("Enter first reading >> ")))
temperatures.append(float(input("Enter second reading >> ")))
temperatures.append(float(input("Enter third reading >> ")))
temperatures.append(float(input("Enter fourth reading >> ")))
temperatures.append(float(input("Enter fifth reading >> ")))
temperatures.append(float(input("Enter sixth reading >> ")))

print("All Temperature Readings Are: ", temperatures)
print("Average Temperature is : ", sp.mean(temperatures))
print("Maximum Temperature is : ", max(temperatures))
print("Minimum Temperature is : ", min(temperatures))