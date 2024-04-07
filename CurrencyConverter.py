from tkinter import *
import requests
import os

'''
Things we could do:
make backgrounds of widgets transparent
fit images better into screen width/height either by scaling the image or changing the window dimensions 
a favorite currencies list
multi-currency converter to look at multiple conversions
offline conversion mode using last fetched rates
enhanced user interface
'''

# Finds image path
def imagePath(directory, imageName):
    
    for root, dirs, files in os.walk(directory):
        if imageName in files:
            return os.path.join(root, imageName)
    return None

# A function that gets the number from entry and then converts it 
def conversion(currencyEntry, dollarEntry, resultLabel):
    # Where usd is the base currency you want to use
    url = 'https://v6.exchangerate-api.com/v6/8e10c7a075c67033b62727da/latest/USD'

    # making a request which pulls the latest conversions
    response = requests.get(url)

    # puts the responses in .json fromat
    data = response.json()

    # set variable 'rates' equal to the 'conversion_rates' part of the .json formatted information
    rates = data['conversion_rates']

    # gets currency you want to convert to
    inputCurrency = currencyEntry.get().upper()

    conversion = 0

    # checks if the inputCurrency is in the rates variable
    # if it is then it sets converision to the correct conversion rate
    if inputCurrency in rates:
        conversion = rates[inputCurrency]
    
    # if it isn't then give error
    else:
        resultLabel.config(text='Error. Input currency is invalid.')

    # calculates the new value with the input conversion
    newCurrency = float(dollarEntry.get()) * conversion

    # displays results
    resultLabel.config(text=f'Converted Amount: {newCurrency} {inputCurrency}')

# print(data)

def main():
    # Create a main window
    root = Tk()
    root.geometry('1000x500')
    root.title('Currency Converter')
    root.config(bg= 'gray')



    searchDirectory = os.path.abspath("./images") # Finds path of images directory
    pngName = "japDragon.png" # What we are looking for in searchDirectory
    path = imagePath(searchDirectory, pngName) # imagePath(directory you want to search in, what you are searching for)
    if path:
        Dragonimg = PhotoImage(file = path)
        Label(root, image=Dragonimg, bg= "gray").place(x=-90, y=50)
        Label(root, image=Dragonimg, bg= "gray").place(x=550, y=50)
    else:
        print("Image not found")

    # Create a label with some text
    titleInfo = Label(root, text="Currency Converter",bg='gray',fg='orange', font=('Microsoft YaHei UI Light' ,30, 'bold'))
    titleInfo.pack(padx=10, pady=10)


    titleNames = Label(root, text='by Karan Patel, Jason Gonzalez, Abdelilah Hanim, Josh Epstein', bg= 'gray', font= ('Microsoft YaHei UI Light', 10))
    titleNames.pack(padx=10, pady=10)

    dollarLabel = Label(root, text='Enter dollar amount: ', bg='gray' ,font=('Microsoft YaHei UI Light', 15))
    dollarLabel.pack()

    dollarEntry = Entry(root)
    dollarEntry.pack()

    currencyLabel = Label(root, text='Enter currency code you want to convert to: ', bg='gray', font= ('Microsoft YaHei UI Light', 12))
    currencyLabel.pack()

    # gets what you want to convert to
    currencyEntry = Entry(root)
    currencyEntry.pack()

    resultLabel = Label(root, text='')
    resultLabel.pack()

    # the lambda function allows us to pass information through the function. 
    conversionButton = Button(root, text='Convert',font=('Microsoft YaHei UI Light', 10), command= lambda: conversion(currencyEntry, dollarEntry, resultLabel))
    conversionButton.pack()

    currencyCodesList = ('Currency Codes of the 10 largest economies: \n \n United States: USD (United States Dollar) \n China, People\'s Republic of: CNY (Chinese Yuan Renminbi) \n Germany: EUR (Euro) \n Japan: JPY (Japanese Yen) \n India: INR (Indian Rupee) \n United Kingdom: GBP (British Pound Sterling) \n France: EUR (Euro) \n Italy: EUR (Euro) \n Brazil: BRL (Brazilian Real) \n Canada: CAD (Canadian Dollar)')

    currencyCodesLabel = Label(root, text=f'{currencyCodesList}', font=('Microsoft YaHei UI Light', 15))
    currencyCodesLabel.pack(padx=10, pady=10)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
