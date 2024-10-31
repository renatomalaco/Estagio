print("Programa para verificar a existência da letra 'a' na frase e conta-la (caso possua)\n")
text = str(input("Insira uma palavra: "))
letter = "a"
text_lower = text.lower()

if letter in text_lower:
    print(f"\nA palavra, {text}, possui a letra A")
    quantity = text_lower.count(letter)
    print(f"{text} possui {quantity} letras 'A'")
else:
    print(f"A palavra, {text}, não possui a letra A")
