def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs - (prijs * korting)
    
    reclame_tekst = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs} euro."
    
    return reclame_tekst
    
print(aanbieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(inkomsten_per_dag, btw):
    totaal_inkomsten = sum(inkomsten_per_dag)

    btw_bedrag = totaal_inkomsten * btw
    
    totaal_bedrag_inclusief_btw = totaal_inkomsten + btw_bedrag

    teruggeefwaarde = f"Het totaal van alle inkomsten van deze week is {totaal_inkomsten} euro, waarover {btw_bedrag} euro btw betaald dient te worden."

    return teruggeefwaarde

inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]
btw_percentage = 0.09
resultaat = inkomsten_totaal(inkomsten_per_dag, btw_percentage)
print(resultaat)

def laag_en_hoog(mijn_lijst):
    
    hoog = max(mijn_lijst)
    laag = min(mijn_lijst)

    resultaat_lijst = [hoog, laag]

    return resultaat_lijst

inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]
resultaat = laag_en_hoog(inkomsten_per_dag)
print(resultaat)

def gemiddelde(mijn_lijst):
   
    gemiddelde_inkomsten = sum(mijn_lijst) / len(mijn_lijst)

    return gemiddelde_inkomsten

inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]
gemiddelde_inkomsten = gemiddelde(inkomsten_per_dag)
print(gemiddelde_inkomsten)
