import censorpy
from censorpy import censor

wordList = ["fuck", "shit", "shat"]

censor = censorpy.censor(words=wordList, remove_zero_width_spaces=True, remove_symbols=True)

print(censor.check("f.u.c.k $hit sh@t"))

