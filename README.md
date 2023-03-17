
# Censor.py
Censor a range of words and phrases with ease, stop people from bypassing censors and more.


## Example:

```bash
import censorpy
wordList = ["fuck", "shit", "shat"]
censor = censorpy.censor(words=wordList, remove_zero_width_spaces=True, remove_symbols=True)
print(censor.check("f.u.c.k $hit sh@t"))
```

```bash
Output: ["fuck", "shit", "shat"]
```

# Note:
Censor.py is NOT currently on pypi meaning you have to install the code manually to use it, I will get it on Pypi soon though
