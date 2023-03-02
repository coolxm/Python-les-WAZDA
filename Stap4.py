def jebentbinnen():
    searchword = input("Welk woord wil je vervangen?: ")
    replaceword = input("Door welk woord?: ")
    filename = "Secretfile.txt"

    text = open(filename).read()
    open(filename, "w").write(text.replace(searchword, replaceword))

def main():
    print("Hallo, wat is jouw naam?")
    naam = input()
    print(f"Dag {naam}")
    
    while True:
        print("Wat is het wachtwoord?")
        wachtwoord = input()
        if wachtwoord == "WAZDA":
            print("Proficiat, je bent binnen! \n")
            jebentbinnen()
            break
        else:
            print("Dat is fout, probeer opnieuw! \n")
main()