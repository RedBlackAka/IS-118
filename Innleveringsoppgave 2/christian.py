
#her starter historien

print("Erling fant ut at silje og sivert er uenighe om teknologivalget i prosjektet.")
print("Han har 2 løsninger for å håntere dette. Den ene er åpen kommunikasjon og den andre er individuelle samtaler.")
print("Erling har ikke så mye tid igjen før prosjektet må leveres og må velge en av disse to løsningene.")
print("hva velger han")

#start av valgmuligheter
#jeg bruker også lower metoden for å gjøre input mindre sensitive og kan skrive i små og store bokstaver

valg = input("åpen kommunikasjon / individuelle samtaler: ").lower()
if valg == "åpen kommunikasjon":
    print("Erling holder et møte med teamet og ha en åpen kommunikasjon for å løse problemene.")
    print("hvilken strategi bør man velge for å løse denne konflikten best og raskest mulig?")
    #valg for åpen kommunikasjon strategi 1 og 2 
    #vis man velger åpen kommunikasjon får mant 2 nye alternativer. strategi 1 og strategi 2

    valgåpenkommunikasjon = input("strategi 1 eller strategi 2: ").lower()
    if valgåpenkommunikasjon == "strategi 1":
        print("Han velger strategi 1. De har en lang diskusjon om hvordan de skal få gjort det men mens de diskuterer")
        print("finner de et nytt problem. Mellom Mandi og jabir. men han har ikke så mye tid igjen og sier til gruppen vi må bare jobbet med prosjektet.")
        print("---------------------------------------------------------------------")
        print("Det ente opp med at de ikke klarte å levere prosjektet i tide.")
    
    elif valgåpenkommunikasjon == "strategi 2":
        print("Han velger strategi 2. De har en diskusjon og Erling er mekler i denne kommunikasjonen i gruppen")
        print("De bruker litt tid men ikke så mye. de finner et nytt problem og løser den fort før de begynner a jobbe med prosjektet")
        print("---------------------------------------------------------------------")
        print("Det endte opp med at de klarte å levere prosjektet i tide.")
    #her slutter valgmulighetene for åpen kommunikasjon
    else:
        print ("Ugyldig valg. Du må velge enten 'strategi 1' eller 'strategi 2'.")
#her starter valgmulighetene for individuelle samtaler

elif valg == "individuelle samtaler":
    print("Erling bestemmer seg for å ta individuelle samtaler med Silje og Sivert for å forstå deres synspunkter bedre.")
    print(" Erling har to strategier han kan velge for å løse denne konflikten.")
    # vis man valgte individuelle samtaler begynner koden her og man kan velge mellom kompromiss-strategi eller samarbeidsorientert problemløsning
   
    valgindividuellesamtaler = input("kompromiss-strategi eller samarbeidsorientert problemløsning: ").lower()
    if valgindividuellesamtaler == "kompromiss-strategi":
        print("Erling velger kompromiss-strategi. Han snakker med både Silje og Sivert individuelt og prøver å finne en løsning.")
        print("Etter en liten stund kommer de frem til en løsning som begge parter kan akseptere.")
        print("---------------------------------------------------------------------")
        print("Det endte opp med at de klarte å levere prosjektet i tide.")
       
    elif valgindividuellesamtaler == "samarbeidsorientert problemløsning":
        print("Erling velger samarbeidsorientert problemløsning. Han oppmuntrer Silje og Sivert til å jobbe sammen for å finne en løsning.")
        print("Etter flere samtaler og diskusjoner klarer sijle og Sivert å finne en løsning men det har brukt for lang tid.")
        print("---------------------------------------------------------------------")
        print("Det endte opp med at de ikke klarte å levere prosjektet i tide.")
    #her slutter valgmulighetene for individuelle samtaler
    else:
        print("Ugyldig valg. Du må velge enten 'kompromiss-strategi' eller 'samarbeidsorientert problemløsning'.")
else:
    print("Ugyldig valg. Vennligst velg enten 'åpen kommunikasjon' eller 'individuelle samtaler'.")
       #begge else er der for å slitte if statment og er der vis noen skriver noe annet en valgmulighetene