pthresh = map(lambda x: x/10.0, range(5,10,1))

ballsz_init = [18, 20, 22, 24]
ballsz_small = [12, 14, 16, 18]
ballsz_large = [24, 26, 28, 30]

presid = [0.5]
bgfg_mode = [0]

allVars = []

pthresh_file = 'pthresh_file1.list'
ballsz_init_file = 'ballsz_init_file1.list'
ballsz_small_file = 'ballsz_small_file1.list'
ballsz_large_file = 'ballsz_large_file1.list'
presid_file = 'presid_file1.list'
bgfg_mode_file = 'bgfg_mode_file1.list'

c = 0

for i in range(1,len(pthresh)):
    for j in range(1,len(ballsz_init)):
        for k in range(1,len(ballsz_small)):
            for m in range(1,len(ballsz_large)):
                for n in range(1,len(presid)):
                    for o in range(1,len(bgfg_mode)):
                        c = c + 1
                        allVars[c,:] = [pthresh(i), ballsz_init(j), ballsz_small(k), ballsz_large(m), presid(n), bgfg_mode(o)]


for i in range(1,len(allVars)):
    fid = open(pthresh_file,'wb')
    fid.write('%f\n',allVars[:,1])
    fid = open(ballsz_init_file,'wb')
    fid.write('%f\n',allVars[:,2])
    fid = open(ballsz_small_file,'wb')
    fid.write('%f\n',allVars[:,3])
    fid = open(ballsz_large_file,'wb')
    fid.write('%f\n',allVars[:,4])
    fid = open(presid_file,'wb')
    fid.write('%f\n',allVars[:,5])
    fid = open(bgfg_mode_file,'wb')
    fid.write('%f\n',allVars[:,6])

fid = open('filenames1.list','wb')

for i in range(1,len(allVars)):
    fid.write('xbrain_paramset_%s_%s_%s_%s_%s_%s\n',str(allVars[i,1]),str(allVars[i,2]),str(allVars[i,3]),str(allVars[i,4]),str(allVars[i,5]),str(allVars[i,6]))
