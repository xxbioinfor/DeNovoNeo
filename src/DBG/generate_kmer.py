import src.util.kmer
import re
re_read = re.compile('^[ATCGN]+$')

#####主程序
group1 = sc.textFile("s3a://synergy.neoantigen.dev.case1/test/PLC_*.fq")
group2 = sc.textFile("s3a://synergy.neoantigen.dev.case1/test/SK*.fq")
ref = sc.textFile("s3a://synergy.neoantigen.dev.case1/test/Homo_sapiens_test.fasta")
#只留下read行
g1 = group1.filter(lambda line:re_read.match(line))
g2 = group2.filter(lambda line:re_read.match(line))
#添加组别编号
g11 = g1.zipWithUniqueId()
g22 = g2.zipWithUniqueId()
#创建kmer
c1 = g11.count()
c2 = g22.count()
rdd1 = g11.flatMap(lambda x: kmer.create_Kmer(x[0],x[1],"H",c1,c2))
rdd2 = g22.flatMap(lambda x: kmer.create_Kmer(x[0],x[1],"T",c1,c2))
rdd3 = rdd1.union(rdd2)
rdd4 = rdd3.reduceByKey(lambda x,y: (kmer.mernum(x[0],y[0]),kmer.mernum(x[1],y[1]),x[2] or y[2]))
rdd4.count()
