def jebentbinnen():
    filename = "Secretfile.txt"
    file = open(filename, "r")
    print("hier is " + filename + "\n")
    for line in file:
        print(line)
    file.close()

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

    jebentbinnen()

main()