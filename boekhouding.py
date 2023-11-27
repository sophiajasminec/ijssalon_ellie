import csv

from helper import onderstreep
from presentatie import presenteer

def presenteer(inkomsten, totaal_inkomsten):
    for ijs_soort, bedrag in inkomsten.items():
        print(f"{ijs_soort}-totaal : {bedrag} euro")
    
    print("==================================")
    print(f"Totaal : {totaal_inkomsten} euro")

inkomsten = {
    "Aardbeien-ijs": 1000,
    "Vanille-ijs": 2000,
    "Chocolade-ijs": 1500,
    "Waterijsjes": 750
}


totaal_inkomsten = sum(inkomsten.values())

presenteer(inkomsten, totaal_inkomsten)

with open("boekhouding.csv’, 'w',newline=") as csvfile:
     for key, value in inkomsten.items():
         writer = csv.writer(csvfile, delimiter=';')
         writer.writerow([key,value])