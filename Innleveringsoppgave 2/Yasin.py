#Du starter storyen med 0 poeng.
poeng=0
#Situasjon 1
print("Konflikten mellom Silje og Sivert.")
print("1 Erling snakker med dem hver for seg først.")
print("2 Han tar det opp i plenum.")

#Sjekker om brukeren har putta inn riktig nummer.
while True:
    valg = input("Skriv nummer her.")
    if valg == "1" or valg == "2":
        break
    else:
        print("Du valgte feil.")
if valg == "1":
    print("De klarer oftere å samarbeide etter et felles møte, og får roet seg litt.")
    poeng+=10
elif valg == "2":
    print("Kan bli bråkete, Silje og Siver kan også føle seg presset. Det blir dårlig stemning, men Erling slipper møte.")
    poeng+=5

#Situasjon 2.
print("Konflikten mellom Hamdi og Jabir.")
print("1 Erling samler dem i et kort møte.")
print("2 Vente og håpe at det går over.")

while True:
    valg = input("Skriv nummer her")
    if valg == "1" or valg == "2":
        break
    else:
        print("Du valgte feil")
if valg == "1":
    print("Begge får sagt hva de egentlig mener, og det blir lettere å rydde opp før situasjonen blir enda værre. ")
    poeng+=10
elif valg == "2":
    print("Konflikten kan sakte men sikkert vokse, og bli enda større lengre fram i tid.")
    poeng+=5

#Situasjon 3
print("Motivasjonen i teamet.")
print("1 Sette av tid til å snakke sammen.")
print("2 Erling sier alle må fokusere 100% på prototypen.")

while True:
    valg = input("Skriv nummer her")
    if valg == "1" or valg == "2":
        break
    else:
        print("Du valgte feil")
if valg == "1":
    print("Folk vil føle seg mer sett og hørt, og kan føre til at samarbeidet blir bedre i det lange løpet.")
    poeng+=10
elif valg == "2":
    print("Teamet jobber fortere i en liten periode, men mange kan bli enda mer slitne. Det skaper dårligere stemning, eller risiko for enda mer konflikt.")
    poeng+=5

#Sjekker poeng og gir deg en konsekvens basert på dine valg.
if poeng == 30:
    print("Beste ending. Her håndteres konflikten tidlig. Teamet blir mer samlet, og prototypen blir ferdig i tide med god kvalitet. Etter dette vil teamet gå videre mot norming-fasen.")
elif poeng > 15:
    print("Middels ending. Her vil noen av konfliktene løses, men andre ikke. Teamet vil fungere, men stemningen vil generelt være litt dårlig. Prototypen vil så vidt bli ferdig, og noen av relasjonene her kan fortsatt være sårbare.")
else:
    print("Om disse valgene blir tatt, kan konflikter bli enda verre. Folk vil samarbeide dårlig, prototypen blir forsinket og hele prosjektet står fast i storming-fasen.")