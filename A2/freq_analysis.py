cipher_text = "PYUJTROZZCJIXTUYXFTOAOOEFOLBCBFZCEXOMTLICTJIXLCJROZYBDTOROZZCGMTYTLCJTOOFCUETOJXXCBSTIYBDTIXBJIXAOOEXFCTTIXJYFXJOPTIXLXAAROZZCCBFBOTYRXFTICTTIXSLXUXPYAAXFLYTIRMHGOCUFJCBFGOOEJIXAQXJIXUXCBFTIXUXJIXJCLZCHJCBFHYRTMUXJIMBDMHOBHXDJFOTJIXTOOEFOLBCNCUPUOZOBXOPTIXJIXAQXJCJJIXHCJJXFYTLCJACGXAAXFOUCBDXZCUZCACFXROZZCGMTTOIXUDUXCTFYJCHHOYBTZXBTYTLCJXZHTSJIXFYFBOTAYEXTOFUOHTIXNCUPOUPXCUOPEYAAYBDJOZXGOFSROZZCJOZCBCDXFTOHMTYTYBTOOBXOPTIXRMHGOCUFJCJJIXPXAAHCJTYT"

english_freq = "ETAOINSRHDLUCMFYWGPBVKXQJZ"

# Frequency Analysis on the cipher text
def create_dictionary2(txt):
    dictionary = {}
    i=0
    for x in set(txt):
        dictionary[x] = txt.count(x)/len(txt)
    return dictionary

test_dict = create_dictionary2(cipher_text)

ciphertext_sorted_freq = list(dict(sorted(test_dict.items(), key=lambda item: item[1], reverse=True)).keys())

ciphertext_to_english_map = {}

for num, letter in enumerate(ciphertext_sorted_freq):
  ciphertext_to_english_map[letter] = english_freq[num]


# Frequency Analysis on the cipher text
def create_ngram_dictionary(txt, ngram):
    dictionary = {}
    
    for i in range(len(txt) - 2):
        word = txt[i: i+ngram]
        dictionary[word] = txt.count(word)
    return dictionary

ciphertext_ngram_dict = create_ngram_dictionary(cipher_text, 2)
print(dict(sorted(ciphertext_ngram_dict.items(), key=lambda item: item[1], reverse=True)))




