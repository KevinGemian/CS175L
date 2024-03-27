def main():
    controlLoop()

def convertToKelvin(fahrenheit):
    #Take in the fahrenheit temp as an argument
    Kelvin = ((fahrenheit - 32) / 1.8) +273.15
    #Convert Fahrenheit to Kelvin
    return Kelvin
    #return Kelvin
    

def convertToCentigrade(fahrenheit):
    #Take in the fahrenheit temp as an argument
    Centigrade = (fahrenheit - 32) / 1.8
    #Convert Fahrenheit to Centigrade
    return Centigrade
    #return Centigrade
    

def doConversion():
    fahrenheit = int(input('Enter Fahrenheit temperature (must be -50 to 130): '))
    #getFahrenheit(), get back Fahrenheit
    convertToKelvin(fahrenheit)
    #convertToKelvin(), send Fahrenheit get back Kelvin
    convertToCentigrade(fahrenheit)
    #ConvertToCentigrade, sends Fahrenheit gets back Centigrade
    print(f'Fahrenheit: {fahrenheit} Kelvin: {convertToKelvin(fahrenheit)} Centigrade: {convertToCentigrade(fahrenheit)}')
    #prints for example: 'Fahrenheit: xx Kelvin xx Centigrade: xx'
    

def repeat():
    repeat = int(input('How many conversions would you like to do this time?: '))
    #Inputs How many conversions would you like to do this time?
    for x in range (repeat):
        doConversion()
    #for x in range how many
        #doConversion()
    

def controlLoop():
    loop = input('Do you want to do some conversions(Yes or No?): ')
    loop = loop.lower()
    #Inputs 'Do you want to do some conversions(Yes or No)?'
    if loop == 'yes':
        repeat()
    #if 'yes' repeat()
    

def getFahrenheit():
    fahrenhiet = int(input('Enter Fahrenheit temperature (must be -50 to 130): '))
    #Inputs 'Enter Fahrenheit temperature (must be -50 to 130): '
    while fahrenhiet < -50 or fahrenhiet > 130:
        fahrenhiet = int(input('Please re-enter: '))
    #(validation loop)'Please re-enter'
    return (fahrenhiet)
    #return Fahrenheit
    

# Call the main function.
if __name__ == '__main__':
    main()
