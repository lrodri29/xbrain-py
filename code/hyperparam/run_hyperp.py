import time
import sys

sys.path.insert(0, '~/xbrain/xbrain-py/code/hyperparam')

from xbrain_hyperparams import xbrain_hyperparams

pthresh = 0.9
ballsz_start = 18
ballsz_small = 12
ballsz_large = 22
presid = 0.5
bgfg = 0

inData = 'cubecutouttest'
pData = 'testpdata'
probData = 'testprobdata'
mapData = 'testmapdata'
nmapData = 'testnmapdata'
vmapData = 'testvmapdata'
centroidOut = 'outputcentroids'
outfilename = 'outfilename'
fileName = 'willisawesome'
errFile = 'temp1.mat'
paintFile = 'temp2.mat'

t = time.time()
xbrain_hyperparams(pthresh, ballsz_start,ballsz_small, ballsz_large,presid, bgfg, fileName, errFile, paintFile, inData, pData, probData, mapData, nmapData, vmapData, centroidOut, outfilename)
elapsed = time.time()-t

print elapsed, 'seconds have passed'
