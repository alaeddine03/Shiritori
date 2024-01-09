# import english words and ignore it if module doesn't exist
try:
    from nltk.corpus import words
    wr = words.words()
except ModuleNotFoundError:
    pass

# shiritori class
class shiritori:
    def __init__(self):
        self.words = []
        self.over = True

# play method
    def play(self, word):
# used try except so if module doesn't exist u can still play
        try:
            if word not in wr:
                print("invalid! - not an english word")
                self.over = False
        except:
            pass
# checking phase
        while self.over:
            if not self.words:
                self.words.append(word)
                return self.words
            elif word in self.words:
                print(word + ' already used')
                self.over = False
            else:
                index = len(self.words) - 1
                current = self.words[index]
                letter = current[-1]
                if word.startswith(letter):
                    self.words.append(word)
                    return self.words
                else:
                    print(f"invalid ! - {word} does not starts with {letter}")
                    self.over = False
        return self.over

# start the game
s = shiritori()
res = True
while (res != False):
    a = input("enter your word : ")
    res = s.play(a)
    print(res)
