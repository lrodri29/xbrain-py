
sb_size_all = [20, 18, 16, 14, 12, 18, 16, 14, 12]
d_size_all =  [ 8, 10, 12, 14, 16, 12, 14, 16, 18]
k = 500


if len(sb_size_all) != len(d_size_all):
    raise RuntimeError('lengths must be equal - change in interface')

for i in range(1,len(sb_size_all)):
    sb_size = sb_size_all[i]
    d_size = d_size_all[i]

    probFile = '~/code/xbrain/data/'
    """ADD SOME DATA FILE HERE"""
    OMP_ProbMap_deploy(probFile, 0.4, sb_size, d_size, k, ['paint_',str(sb_size), '_', str(d_size), '.py'], ['centroid_',str(sb_size), '_', str(d_size), '.py']);
