#anagrams

def verify_two_strings(str1,str2):
    ana_table = {key:0 for key in string.ascii_lowercase}

    for i in str1:
        ana_table[i] += 1
    for i in str2:
        ana_table[i] -= 1

    if len(set(ana_table.values())) <2:
        return True
    else:
        return False

def test_verify_two_strings():
    str1 = 'marina'
    str2 = 'aniram'
    assert(verify_two_strings(str1, str2)==True)
    str1 = 'google'
    str2 = 'gougle'
    assert(verify_two_strings(str1,str2) == False)
    print('Passes')

if __name__== '__main__':
    test_verify_two_strings()
