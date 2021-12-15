#emoji converter, idea by programming with mosh

conver = input("> ")#input for program
words  = conver.split(' ')
emojis ={
":)": "🙂",
":(": "☹️",
":*": "😘",
":'(": "😢"
}
result = ""
for word in words:
    result += emojis.get(word, word) + " "
print(result)
