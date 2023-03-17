import censorpy
from censorpy import censor

wordList = ["fuck", "shit", "shat"]

censor = censorpy.censor(words=wordList, remove_zero_width_spaces=True, remove_symbols=True, change_character="*")

print(censor.censor("$hit i stubbed my toe, f.u.c.k"))