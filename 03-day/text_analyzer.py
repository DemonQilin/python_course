print("------TEXT ANALYZER------\n")
text = input("Type a text to analyze:\n> ")

print("\nNow, you have to type 3 letters to analyze")
letters = [input("First letter: > "), input("Second letter: > "), input("Third letter: > ")]
print(f"letters: {letters}")

response = {
    f"Total appearances of \"{letters[1]}\"": text.lower().count(letters[1].lower()),
    f"Total appearances of \"{letters[0]}\"": text.lower().count(letters[0].lower()),
    f"Total appearances of \"{letters[2]}\"": text.lower().count(letters[2].lower()),
    'Total words': len(text.split()),
    'First letter': text[0],
    'Last letter': text[-1],
}

reversed_text = text.split()
reversed_text.reverse()
reversed_text = ' '.join(reversed_text)
response['Reversed text'] = reversed_text
response['Pyton is in text'] = 'python' in text.lower()

print(response)

