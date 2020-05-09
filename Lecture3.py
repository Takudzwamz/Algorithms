import os.path


def Naive_Z_Values(S):
    n = len(S)
    zp=[0]
    for i in range(1,n):
        j = i
        while j < n and S[j] == S[j - i]:
            j+=1
        zp.append(j - i)
    print("Naive_Z_Values", zp)


def Prefix_Z_Values(S):
    n = len(S)
    l =0
    r= 0
    zp=[0]*n
    for i in range(1,n):
        zp[i]=0
        if i >= r:
            #Позиция i не покрыта Z-блоком – он вычисляется заново
            zp[i] = StrComp(S,n,0,i)
            l=i
            r = l + zp[i]
        else:
            # Позиция i покрыта Z-блоком – он используется 
            j= i-l
            if zp[j] < r - i:
                zp[i] = zp[j]
            else:
                zp[i] = r - i + StrComp (S, n, r - i, r)
                l = i 
                r = l + zp[i]
    print("Prefix_Z_Values",zp)
    return zp

def StrComp(S,n,i1,i2):
    eqLen = 0
    try:
      while i1 < n and i2 < n and S[i1] == S[i2]:
        eqLen += 1
        i1 += 1
        i2 += 1
    except IndexError:
        return eqLen
    else:
         return eqLen

def Suffix_Z_Values(S):
    n=len(S)
    l=r=n-1
    zs=[0]*(n-1)
    for i in range(n-2,0,-1):
        #zs[i]=0
        if i<=l:
            zs[i] = StrCompBack (S, i, n-1)
            r = i 
            l = r - zs[i]
        else:
            j = n - (r + 1 - i)
            if zs[i]<i-l:
                zs[i]= zs[j]
            else:
                zs[i] = i - l + StrCompBack (S, l, n - i + l)
                r = i 
                l = r - zs[i]
    print("Suffix_Z_Values",zs)
    return zs

#Наибольшая длина совпадающих подстрок
def StrCompBack(S,i1,i2):
    eqLen = 0
    try:
        while i1 >=0 and i2 >=0 and S[i1-1] == S[i2-1]:
           eqLen += 1
           i1 -= 1
           i2 -= 1
    except IndexError:
        return eqLen
    else:
        return eqLen

def ZP_to_BPM(zp,n):
    bpm = [0]*n#Инициализация
    for i in range(0,n):
        bpm[i]=0
    for j in range(n-1,0,-1):
        i = j + zp[j] - 1 
        bpm[i] = zp[j]
    print("ZP_to_BPM",bpm)
    return bpm

def ZP_to_BP(zp,n):
    bp = [0]*n#Инициализация
    for i in range(0,n):
        bp[i]=0
    for j in range(1,n):
        for i in range(j+zp[j]-1,j-1,-1):
            if bp[i]:
                break
            bp[i]=i-j+1
    print("ZP_to_BP",bp)
    return bp
    

def BP_to_ZP(bp,n):
    l=0
    r=0
    zp=[0]*n
    for i in range(1,n):
        #zp[i]=0
        if i>=r:
            zp[i] = ValGrow (bp, n, i, 1)
            l=i
            r=l
            r=l+zp[i]
        else:
            j=i-l
            if zp[j]<r-i:
                zp[i]=zp[j]
            else:
                zp[i] = r - i + ValGrow (bp, n, r, r - i - 1)
                l=i
                r=l
                r=l+z[i]
    print("BP_to_ZP",zp)
    return zp


def ValGrow(nArr,n,nPos,nVal):
    nSeqlen=0
    try:
        while nPos < n & nArr[nPos] == nVal:
            nSeqlen += 1
            nPos += 1
            nVal += 1
    except IndexError:
        return nSeqlen
    else:
        return nSeqlen

def open_file():
    while 1:
        try:
            file = input("Choose File: ")
            if not os.path.exists(file):
                raise FileNotFoundError(file)
            break
        except FileNotFoundError:
            print("File does not exist")
    with open(file, 'r') as input_string:
        in_line = ''
        for line in input_string:
            for letter in line:
                if letter is '\n':
                    continue
                in_line += letter
    return in_line



if __name__ == "__main__":
    input_line = open_file()
    print("Initial File", input_line.upper())

    Naive_Z_Values(input_line)
    zp = Prefix_Z_Values(input_line)
    Suffix_Z_Values(input_line)
    ZP_to_BPM(zp, len(input_line))
    bp = ZP_to_BP(zp, len(input_line))
    BP_to_ZP(bp, len(input_line))


    #taku