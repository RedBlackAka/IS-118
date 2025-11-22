print("\nErling har satt sammen teamet sitt og forbereder seg på eventuelle konflikter.")

#Første ledd
print("\nKonflikt 1: Det oppstår en konflikt mellom UI/UX designeren Silje og IT-rådgiveren Sivert. ")

valg1 = input("\nErling vurderer om han skal løse det individuelt eller i felleskap. Hvilket alternativ burde han velge?\n"
              "\n1. Individuelt"
              "\n2. Fellesskap\n").strip().lower()

if valg1 in ["1","1.","individuelt"]:
    løsning1 = "indiv"
    print("\nHan tar det individuelt, men det skaper tidspress.")
elif valg1 in ["2","2.","fellesskap"]:
    løsning1 = "felles"
    print("\nHan tar det opp felles.")
else:
    løsning1 = "null"
    print(f"\nDu kommer med forslaget {valg1}? Teamet er forvirret og faller fra hverandre.")

#Andre ledd vis problemet løses individuelt
if løsning1 == "indiv":
    print("\nKonflikt 2.1: Prosjektet har nå begrenset tid.")

    valg2 = input("\nErling vurderer å håndtere dette gjennom en kompromiss-strategi eller en samarbeidsorientert problemløsning. Hvilket alternativ burde han velge?\n"
                  "\n1. Kompromiss-strategi"
                  "\n2. Samarbeidsorientert problemløsning\n").strip().lower()

    if valg2 in ["1","1.","kompromiss-strategi"]:
        løsning2 = "kompstra"
        print("\nDe løser konfilkten med en kompromiss-strategi.")
    elif valg2 in ["2","2.","samarbeidsorientert problemløsning"]:
        løsning2 = "samløsning"
        print("\nDe løser konflikten med en samarbeidsorientert problemløsning.")
    else:
        løsning2 = "null"
        print(f"\nDu kommer med forslaget {valg2}? Teamet er forvirret og faller fra hverandre.")

#Tredje ledd vis problemet løses i felleskap
elif løsning1 == "felles":
    print("\nKonflikt 2.2: Problemet er ikke helt løst enda og hele teamet føler nå på usikkerhet.")

    valg3 = input("\nErling vurderer løsning gjennom strategi 1 eller 2. Hvilket alternativ burde han velge?\n"
                  "\n1. Strategi 1"
                  "\n2. Strategi 2\n").strip().lower()

    if valg3 in ["1","1.","strategi 1"]:
        løsning3 = "stra1"
        print("\nDe løser konflikten med strategi 1.")
    elif valg3 in ["2","2.","strategi 2"]:
        løsning3 = "stra2"
        print("\nDe løser konflikten med strategi 2.")
    else:
        løsning3 = "null"
        print(f"\nDu kommer med forslaget {valg3}? Teamet er forvirret og faller fra hverandre.")

#Sjekk alle resultat av løsninger og print endelig resultat
if løsning1 == "indiv":
    if løsning2 == "kompstra":
        print("\nKonflikten er helt løst og prosjektet klarer seg videre.")
    elif løsning2 == "samløsning":
        print("\nProsjektet ender opp å ta for lang tid og blir ikke fullført.")
elif løsning1 == "felles":
    if løsning3 == "stra1":
        print("\nDet oppstår tidspress og prosjektet blir ikke fullført.")
    elif løsning3 == "stra2":
        print("\nKonfilkten er helt løst og prosjektet klarer seg videre.")