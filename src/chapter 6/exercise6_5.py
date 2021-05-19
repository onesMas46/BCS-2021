str = "X-DSPAM-Confidence:0.8475 "
akpos = str.find(":")
print(akpos)
piece = str[akpos+1:]
print(piece)
value = float(piece)
print(value + 42.0)