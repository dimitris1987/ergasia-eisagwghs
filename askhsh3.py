
inText = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρστυφχψω"
outText = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklmΞΟΠΡΣΤΥΦΧΨΩΑΒΓΔΕΖΗΘΙΚΛΜΝξοπρστυφχψωαβγδεζηθικλμν"
rot13 = str.maketrans(inText, outText)

message = input("Γράψτε το κείμενο που θέλετε να κωδικοποιήσετε\n")
print("Το κωδικοποιημένο κείμενο ειναι: "+message.translate(rot13))