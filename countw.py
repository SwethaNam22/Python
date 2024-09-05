def count_word(strr):
    global countw
    countw=dict()
    allw=strr.lower()
    allw=strr.strip()
    allw=strr.split()
    for i in allw:
        if i in countw:
            countw[i] += 1
        else:
            countw[i]=1
    return countw
strn='''The modern Olympic Games or Olympics (French: Jeux olympiques)[a][1] are the leading international sporting events featuring summer and winter sports competitions in which thousands of athletes from around the world participate in a variety of competitions. The Olympic Games are considered the world's foremost sports competition with more than 200 teams, representing sovereign states and territories, participating. By default, the Games generally substitute for any world championships during the year in which they take place (however, each class usually maintains its own records).[2] The Olympic Games are held every four years. Since 1994, they have alternated between the Summer and Winter Olympics every two years during the four-year Olympiad.'''
count_word(strn)
n=str(input("enter the word you want to search"))
if n in countw:
    x=countw.get(n)
    print(x)





