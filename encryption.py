text="aeiou"
code=" "
for ch in text:
    a=ord(ch)
    c=a-5
    code=code+chr(c)
print(code)
