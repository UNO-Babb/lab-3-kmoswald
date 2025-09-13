#TempConvert.py
#Name:Kaitlyn Oswald
#Date:9/12/25
#Assignment: Lab 3


def main():
  #Prompt the user for a Fahrenheit temperature
  tempF = float(input("Enter a temperature in Fahrenheit"))
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.

  tempC = round(tempF * 1.8 + 32, 1)
  
  print(tempF, "is ", tempC, "degrees celsius.")

if __name__ == '__main__':
  main()
