print("Hallo, wat is jouw naam?")
naam = input()
print(f"Dag {naam}")

print("Wat is het wachtwoord?")
wachtwoord = input()

if wachtwoord != "WAZDA":
    print("Dat is fout, probeer opnieuw!")
else:
    print("Proficiat, je bent binnen!")