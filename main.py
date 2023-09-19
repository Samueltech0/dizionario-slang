meme_dict = {
    "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
    "LOL": "Una risposta comune a qualcosa di divertente",
    "SHEESH": "Leggera disapprovazione",
    "CREEPY": "Spaventoso, inquietante",
    "PARA": "Preoccuparsi per qualcosa, paranoiarsi",
}

def meme():
    while True:
        parola = input("Scrivi una parola che non capisci (usa solo lettere maiuscole!): ")
        if parola in meme_dict:
            print(parola, meme_dict[parola])
        else:
            print("La parola inserita non è presente all'interno del mio database")
            
        x = input("Vuoi continuare? y or n: ")
        if x == "n":
            print("Arrivederci!")
            break
        elif x != "y":
            print("Scelta non valida, il programma continuerà.")
            
meme()
