import datetime

hmeres = ["Δευτέρα","Τρίτη","Τετάρτη","Πέμπτη","Παρασκευή","Σάββατο","Κυριακή"]
mhnes = ["Ιανουάριο", "Φεβρουάριο","Μάρτιο","Απρίλιο","Μάϊο","Ιούνιο","Ιούλιο","Αύγουστο","Σεπτέμβριο",
         "Οκτώβριο","Νοέμβριο","Δεκέμβριο"]
hmera = datetime.datetime.today().weekday()
dayN = datetime.datetime.today().day
mhnas = datetime.datetime.today().month
etos = datetime.datetime.today().year
print("Σήμερα έχουμε "+str(dayN)+", ημέρα "+hmeres[hmera]+", μήνα "+mhnes[mhnas-1]+", έτος "+str(etos))

sum = 0
for i in range(etos+1, etos+11):
    if datetime.datetime(i, mhnas, dayN).weekday() == hmera:
        sum +=1

print("Για τα επόμενα 10 χρόνια θα τύχει "+str(sum)+" φορές να είναι "+hmeres[hmera]+" και "+str(dayN)+" για τον μήνα "+mhnes[mhnas-1])