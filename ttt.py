def checker(line,word):    
    flag = False
    if word=='':
        return True
    if line[0]==word[0]:
        return checker(line[1:],word[1:])
    else:
        return False
    

word = input('Enter the word you want to search for : ')

file_name = input('Enter filename : ')

file_content = open(file_name,'r')

count = 0

for line in file_content:
    f = 0
    for i in range(len(line)-1):
        
        if checker(line[i:],word):
            f = 1
            count = count+1
            
    if f: print(line)
            
        
print('Total count of word is ',count)