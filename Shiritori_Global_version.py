# shiritori class
class shiritori:
    def __init__(self):
        self.words = []
        self.over = True

# play method
    def play(self, word):
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
