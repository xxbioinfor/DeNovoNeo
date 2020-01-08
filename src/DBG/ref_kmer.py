import src.util.kmer
referenceTestFile = sc.textFile("s3a://synergy.neoantigen.dev.case1/test/Homo_sapiens*")

referenceList = referenceTestFile.collect()
refCount = referenceTestFile.count()
referenceNew = sc.parallelize(kmer.ref_read(referenceList,refCount))
referenceFile = referenceTestFile.union(referenceNew)
referenceFile = referenceFile.filter(lambda line:kmer.ref_del(line))
ref_mer = referenceFile.map(lambda x: kmer.create_ref_Kmer(x))
ref_mer.count()