løsning1 = "Dette tar for lang tid og teamet rekker ikke å fremstille den førstep prototypen i tide"
løsning2 = "Konflikten roer seg og temaet går inn i norming - fasen før fremstilling av prototypen"
løsning3 = "Det oppstår en ny konflikt, prototypen når ikke opp til forventet nivå"

print("Det er oppstått en konflikt i arbeidsgruppen mellom UI/UX designeren Silje og IT-rådgiveren Sivert. \n" \
"Erling vurderer om han skal løse det individuelt eller i fellesskap. Hvilket alternativ burde han velge?\n" \
    "\n1. Individuell"
    "\n2. Fellesskap\n")
valg1 = input("").strip().lower()
if valg1 in ["1","Individuell"]:
    svar1 = "Individuell"
    print("du velget å løse konflikten individuelt, du kan velge mellom to strategier for å håndtere konflikten videre.\n"
        "1. kompromiss - strategi\n"
        "2. samarbeidorientertproblemløsning\n"
          )
elif valg1 in ["2","Fellesskap"]:
    svar1 = "Fellesskap"
    print("du velgert å løse konflikten i fellesskap, du kan velge mellom to strategier for å håndtere konflikten videre.\n"
        "1. Strategi 1\n"           
        "2. Strategi 2\n")
else:
    print("Plis velg alternativ 1 eller 2")

if svar1 == "Individuell":
    valg2 = input("").strip().lower()
    if valg2 in ["1","kompromiss - strategi"]:
        svar2 = "kompromiss - strategi"
        print(f"du valgte kompromiss-strategien, dette innebærer at begge parter gir og tar litt for å nå en løsning.\n{løsning2}")
    elif valg2 in ["2","samarbeidorientertproblemløsning"]:
        svar2 = "samarbeidorientertproblemløsning"
        print(f"du valgte samarbeidorientert-strategien, dette innebærer at begge parter jobber sammen for å finne en løsning som tilfredsstiller begge parter fullt ut.\n{løsning1}")
    else: 
        print("Plis velg alternativ 1 eller 2")
elif svar1 == "Fellesskap":
    valg2 = input("").strip().lower()
    if valg2 in ["1","strategi 1"]:
        svar2 = "strategi 1"
        print(f"du valgte strategi 1, dette innebærer at begge parter gir og tar litt for å nå en midlertidig løsning.\n{løsning3}")
    elif valg2 in ["2","strategi 2"]:
        svar2 = "strategi 2"
        print(f"du valgte strategi 2, dette innebærer at du går inn som mekler og hjelper begge parter med å finne en løsning som er akseptabel for begge.\n{løsning2}")
    else: 
        print("Plis velg alternativ 1 eller 2")