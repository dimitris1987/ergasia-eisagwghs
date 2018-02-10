import random
import string

pinakas = []
lekseis =[]
#Δημιουργία του πίνακα
for i in range(100):
    s=""
    for j in range(100):
        s+=str(random.choice(string.ascii_uppercase))
    pinakas.append(s)
onomaArxeiou = input("Πληκτρολογήστε το όνομα του αρχείου που θέλετε να σκανάρετε\n")


with open(onomaArxeiou, "r") as f:
    for line in f:
        #διαβάζει τις γραμμές
        for grammh in pinakas:
            if line.strip().upper() in grammh:
                if line not in lekseis:
                    lekseis.append(line)
        #μετατρέπει την στήλη σε string
        for i in range (100):
            sthlh=""
            for x in pinakas:
                sthlh+=str(x[i])
        #διαβαζειτην στήλη
        if line.strip().upper() in sthlh:
            if line not in lekseis:
                lekseis.append(line)

if len(lekseis)>0:
    print("Οι λέξεις του αρχείου "+onomaArxeiou+" που περιέχονται στο τετράγωνο είναι οι κάτωθι:")
    for l in lekseis:
        print(l)
else:
    print("Καμία λέξη δεν περέχεται στο τετράγωνο")