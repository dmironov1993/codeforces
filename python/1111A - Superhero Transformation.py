a = input()
b = input()
vowel = 'aeiou'
print ('YES' if len(a) == len(b) and all(((c in vowel) == (d in vowel) for c,d in zip(a,b))) else 'NO')
