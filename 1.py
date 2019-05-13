with open ('./log_files/201811113035M.log',encoding='utf_8') as f:
    x=0
    for line in f:
        id1=line.split(',')[1]
        id2=id1.split('：')[1]
        if id2=='201811113035M':
            x+=1
    print(x)

