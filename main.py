import gtts
from playsound import playsound

text = input("Jazin': ")

u = list(text)

print(u)

neednot = {
    'b': 'б',
    'v': 'в',
    'd': 'д',
    'e': 'е',
    'j': 'дж',
    'z': 'з',
    'y': 'й',
    'k': 'к',
    'q': 'к',
    'l': 'л',
    'm': 'м',
    'p': 'п',
    'r': 'р',
    's': 'с',
    't': 'т',
    'w': 'у',
    'f': 'ф',
    'x': 'х',
    'h': 'х',
    'c': 'ц',

    "a": "а",
    "g": "г",
    "n": "н",
    "o": "о",
    "u": "у",
    "i": "ы",
}

needed1 = {
    "a'": "а",
    "g'": "г",
    "n'": "н",
    "o'": "о",
    "u'": "у",
    "i'": "и",
}

needed2 = {
    'sh': 'ш',
    'ch': 'ч'
}

for i in range(len(u)-1):
    if u[i] == 's' and u[i+1] == 'h':
        u.pop(i)
        u.insert(i, "ш")
        u.pop(i + 1)
    if u[i] == 'c' and u[i + 1] == 'h':
        u.pop(i)
        u.insert(i, "ч")
        u.pop(i + 1)

def remove(self):
    if "'" in self:
        self.remove("'")
remove(u)

for k, v in neednot.items():
    for i in range(len(u)-1):
        if u[i] == k:
            u.insert(i, v)
            u.pop(i+1)
        if u[-1] == k:
            u.insert(-1, v)
            u.pop(-1)

tz = ''.join(u)
print(tz)

tts = gtts.gTTS(tz, lang='ru')
tts.save("hello.mp3")
playsound("hello.mp3")