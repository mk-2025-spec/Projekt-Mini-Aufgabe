def bmiRechner():
    bmiverlauf = []  
    anzahl = int(input("Wie viele BMI-Werte möchtest du berechnen? ")) 
    
    for i in range(anzahl):
        print(f"Berechnung {i + 1}:")
        gewicht = float(input("Gib dein Gewicht in kg ein: "))
        groesse = float(input("Gib deine Größe in Meter ein: "))
        bmi = gewicht / (groesse ** 2)
        bmiverlauf.append(bmi) 
        print(f"Dein BMI beträgt: {bmi:.2f}")
    
    print("\nVergleich der BMI-Werte:")
    for index, wert in enumerate(bmiverlauf):
        print(f"BMI {index + 1}: {wert:.2f}")
    print(f"Durchschnittlicher BMI: {sum(bmiverlauf) / len(bmiverlauf):.2f}")
    print(f"Höchster BMI: {max(bmiverlauf):.2f}")
    print(f"Niedrigster BMI: {min(bmiverlauf):.2f}")

    


bmiRechner()

