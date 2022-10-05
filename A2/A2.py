text = "PYUJTROZZCJIXTUYXFTOAOOEFOLBCBFZCEXOMTLICTJIXLCJROZYBDTOROZZCGMTYTLCJTOOFCUETOJXXCBSTIYBDTIXBJIXAOOEXFCTTIXJYFXJOPTIXLXAAROZZCCBFBOTYRXFTICTTIXSLXUXPYAAXFLYTIRMHGOCUFJCBFGOOEJIXAQXJIXUXCBFTIXUXJIXJCLZCHJCBFHYRTMUXJIMBDMHOBHXDJFOTJIXTOOEFOLBCNCUPUOZOBXOPTIXJIXAQXJCJJIXHCJJXFYTLCJACGXAAXFOUCBDXZCUZCACFXROZZCGMTTOIXUDUXCTFYJCHHOYBTZXBTYTLCJXZHTSJIXFYFBOTAYEXTOFUOHTIXNCUPOUPXCUOPEYAAYBDJOZXGOFSROZZCJOZCBCDXFTOHMTYTYBTOOBXOPTIXRMHGOCUFJCJJIXPXAAHCJTYT"
guess = ""
result = ""
for letter in text:
    if letter.upper() in alphabet:
        result += key[alphabet.find(letter.upper())]
    else:
        result += letter
print(result)

#1. TRY: replace X with E -- such they appear the most: 
guessCIPHER = "X"
guessTEXT = "E"
for letter in text:
    if letter.upper() in guessCIPHER:
        guess += guessTEXT[guessCIPHER.find(letter.upper())]
    else:
        guess += letter
print("GUESS: " + guess)
print(" ------------------------ ")

#2. THEN, try replace TIX --> THE (our second guess)
guess = ""
guessCIPHER = "TIX"
guessTEXT = "THE"
for letter in text:
    if letter.upper() in guessCIPHER:
        guess += guessTEXT[guessCIPHER.find(letter.upper())]
    else:
        guess += letter
print("GUESS 2: " + guess)
print(" ------------------------- ")

#3. THEN, try other commonly occured words (2 letters): TO --> TO (Guess) ALSO based on the histogram frequency.
# we don't do anything

#4. Given that THAT there's at least one COMMA (given by TA), we can scan for _O___ occurences and replace
# COMMA for _O___. This occurs at the 'ROZZC'. CONTROL-F of this yields several occurences of this.
guess = ""
guessCIPHER = "ROZZCTIX"
guessTEXT = "COMMATHE"
for letter in text:
    if letter.upper() in guessCIPHER:
        guess += guessTEXT[guessCIPHER.find(letter.upper())]
    else:
        guess += letter
print("GUESS 4: " + guess)
print(" ------------------------- ")
