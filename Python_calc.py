import math
class C:
    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    B = '\033[94m'
    END = '\033[0m'

while True:
    print()
    print(C.Y+"Taschenrechner"+C.END)
    print(C.Y+"=============="+C.END)
    print()
    def get_colored_input(prompt, color):
     return input(color + prompt + C.END)
    try:
        user_input1 = get_colored_input("Zahl eingeben: ", C.B)
        Rechenzeichen = get_colored_input("Rechenzeichen; + - * / ** sqrt eingeben: ", C.B)

        Nummer1=float(user_input1)
    
        if Rechenzeichen == "sqrt":
            result = math.sqrt(Nummer1)
            endresult = "{:.4f}".format(result)
        else:
            user_input2 = get_colored_input("Zahl eingeben: ", C.B)
            Nummer2 = float(user_input2)

        if Rechenzeichen== "+":
            result=Nummer1+Nummer2

        elif Rechenzeichen == "sqrt":
            result = math.sqrt(Nummer1)

        elif Rechenzeichen== "*":
            result=Nummer1*Nummer2

        elif Rechenzeichen== "**":
            result=Nummer1**Nummer2

        elif Rechenzeichen== "-":
            result=Nummer1-Nummer2

        elif Rechenzeichen== "/":
            if Nummer2 != 0:
                result=Nummer1/Nummer2
            else:
                raise ZeroDivisionError("Kann nicht durch null teilen")
        else:
            raise ValueError ("Ungueltiges Rechenzeichen")

        if result.is_integer():
            endresult = "{:.0f}".format(result)
        else:
            endresult = "{:.4f}".format(result)

        print()
        print(C.G+"Ergebnis:", endresult, C.END)

    except ValueError as e:
        print(C.R + "Fehler (ValueError):", e, C.END)
    except ZeroDivisionError as zde:    
        print(C.R + "Fehler (ZeroDivisionError):", zde, C.END)
    except Exception as e:
        print(C.R + "Ein unerwarteter Fehler ist aufgetreten:", e, C.END)

    user_choice = get_colored_input("Möchten Sie eine weitere Berechnung durchführen? (j/n): ", C.B)
    if user_choice.lower() != 'j':
            break