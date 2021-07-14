def scramble(s1, s2):
    return True if (''.join([el for el in s2 if el in s1])) == s2 else False





print(scramble('rkqodlw', 'world')) #,  True)
print(scramble('cedewaraaossoqqyt', 'codewars')) #, True)
print(scramble('katas', 'steak')) #, False)
print(scramble('scriptjava', 'javascript')) #, True)
print(scramble('scriptingjava', 'javascript')) #, True)