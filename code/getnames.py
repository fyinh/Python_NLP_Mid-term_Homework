import codecs

f = open('三国演义人物表.txt','r',encoding='utf-8')
data = f.readlines()
f.close()
TotalNames = []
FirstNames = ['皇甫','司马','夏侯','公孙','诸葛']
for names in data:
    if names == '\n':
        continue
    names = names.strip('\n')
    names = names.strip('\ufeff')
    names = names.replace('\u3000',' ')
    Names = names.split('） ')
    if len(Names) > 1:
        for name in Names:
            name = name.split('（')
            na = name[0].replace(' ', '')
            TotalNames.append(na)
    else:
        Nams = Names[0].split('  ')
        for name in Nams:
            na = name.replace(' ','')
            TotalNames.append(na)
# print(len(TotalNames),TotalNames)
namefile = open('names.txt','w',encoding='utf-8')
for nb in TotalNames[0:len(TotalNames)-1]:
    namefile.write(nb+',nr\n')
namefile.close()



