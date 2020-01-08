import re
re_read = re.compile('^[ATCGN]+$')
re_ref = re.compile('^\>|^[N]+$')
re_head = re.compile('^\>')
re_N = re.compile('N')

def ref_del(line):
    if re_ref.match(line):
        return False
    else:
        return True

def ref_read(reference,count):
    refRead = []
    for i in range(count-1):
        if re_head.match(reference[i] or re_head.match(reference[i+1])):
            continue
        else:
            if len(reference[i+1]) >= 44:
                read = reference[i][-44:]+reference[i+1][0:44]
                refRead.append(read)
            else:
                read = reference[i][-44:]+reference[i+1]
                refRead.append(read)
    return refRead

def create_ref_Kmer(read):
    l=[]
    for index in range(len(read)-44):
        t=0
        t = read[index:index+45]
        if re_N.match(t):
            continue
        else:
            l.append((t))
            l.append((revcomp(t)))
    return l

def create_Kmer(read,num,grp,c1,c2):
    l=[]
    for index in range(len(read)-44):
        kmer =[read[index:index+45],([0 for x in range(c1)],[0 for x in range(c2)],0)]
        if grp=="H":
            kmer[1][0][num] = 1
        if grp=="T":
            kmer[1][1][num] = 1
        kmer1 = kmer
        kmer1[0] = revcomp(kmer[0])
        l.append(kmer)
        l.append(kmer1)
    return l

def revcomp(seq):
    basecomplemt = {
        "A":"T",
        "T":"A",
        "G":"C",
        "C":"G",
    }
    Letters = list(seq)
    Letters = [basecomplemt[base] for base in Letters]
    s = ''.join(Letters)
    return s[::-1]

def mernum(l1,l2):
    l = []
    for i in range(len(l1)):
        l.append(l1[i] or l2[i])
    return l