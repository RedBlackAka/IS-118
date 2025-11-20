indiv = "Individuell"
felles = "Fellesskap"
kompromiss = "kompromiss - strategi"
samarbeid = "samarbeidorientert - strategi"
felleskompromiss = "felleskompromiss - strategi"
mekler = "mekler - strategi"

print("Det har oppstått en skummel konflikt mellom to parter i teamet til Erling. Silje og Sivert er uening i hvordan prosjektet skal fremstilles. Konflikten er en sakskonflikt, men bør ikke utvlikles til en sakskonflikt. \n")

print("Erling vurderer om han skal løse det individuelt eller i felleskap i teamet. Hvilket alternativ burde han velge?\n"
        "\n1. Individuell"   
        "\n2. Fellesskap\n")
valg1 = input("").strip().lower()
if valg1 in ["1.","1","Individuell"]:
    løsning1 = indiv
    print("Du valgte å løse konflikten individuelt, Erling må nå velge mellom to strategier for å håndtere konflikten videre.\n"
        "1. kompromiss - strategi\n"
        "2. samarbeidorientert - strategi\n"
          )
    valg2 = input("").strip().lower()
    if valg2 in ["1.","1","kompromiss - strategi"]:
        løsning2 = kompromiss
        print("Du valgte kompromiss-strategien, dette innebærer at begge parter gir og tar litt for å nå en midlertidig løsning. Resultatet av kompromiss-strategien er at prosjektet klarer å flytte videre til normeringsfasen. Dette er et resultat av at Sivert og Silje legger fra seg det de setter minst viktigst for dem i prosjektet og at sakskonflikten slipper å bli en personkonflikt. Motivasjonen i teamet øker ettersom at Erling viste at han kan ta en rask avgjørelse.")
    elif valg2 in ["2.","2","samarbeidorientert - strategi"]:
        løsning2 = samarbeid
        print("Du valgte samarbeidorientert-strategien, dette innebærer at begge parter jobber sammen for å finne en løsning som tilfredsstiller begge parter fullt ut. Resultatet av den samarbeidsorienterte strategien er at prototypen i prosjektet ikke rekker å fremstilles. Etter lang tid klarer Sivert og Silje å bli enige og beslutningen blir håndtert på en grundig nok måte at de slipper å utløse en personkonflikt. Likevel har tiden rent ut.")
    else: 
        print("Plis velg alternativ 1 eller 2")
  
elif valg1 in ["2.","2","Fellesskap"]:
    løsning1 = felles
    print("du velger å løse konflikten i fellesskap, Erling kan velge mellom to strategier for å håndtere konflikten videre.\n" \
        "1. kompromiss - strategi\n"
        "2. mekler - strategi\n")
    valg2 = input("").strip().lower()
    if valg2 in ["1.","1","kompromiss - strategi"]:
        løsning2 = felleskompromiss
        print("Du valgte kompromiss-strategien, dette innebærer at begge parter gir og tar litt for å nå en midlertidig løsning. Gruppen ble ikke effektiv nok til å klare å levere en prototype av produkt innen tidsfristen.")
    elif valg2 in ["2.","2","mekler - strategi"]:
        løsning2 = mekler
        print("Du valgte mekler-strategien, dette innebærer at en nøytral tredjepart hjelper begge parter med å finne en løsning som er akseptabel for begge. Gruppen ble ikke så fornøyd, men folk vet hva de skal jobbe med og Erling gir siste ord om hvordan man skulle gjøre ting i prosjektet. så motivasjonen ble høy i en kort periode og det var nok tid til at prosjektet fikk fremstille en prototype i tide.")
    else: 
        print("Velg alternativ 1 eller 2")
else:
    print("Velg alternativ 1 eller 2")