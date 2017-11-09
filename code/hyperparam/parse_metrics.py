from matplotlib import numpy

baseDir1 = '/Users/evadyer/Documents/xbrain-hyperpresults/ec2_2015November09_02h02m26s498ms';
f1 = dir([baseDir1, '*.py'])

baseDir2 = '/Users/evadyer/Documents/xbrain-hyperpresults/bc1_2015November08_19h12m51s242ms';
f2 = dir([baseDir2, '*.py'])

baseDir3 = '/Users/evadyer/Documents/xbrain-hyperpresults/ilastik3';
f3 = dir([baseDir1, '*.py'])

metrics = [];
for i in range(1,len(f1)):
    load([baseDir1, f1(i).name])
    metrics(end+1).segErrNMap = segErrNMap
    metrics(end).segErrTMap = segErrTMap
    metrics(end).CellMetrics_CentroidErr = CellMetrics.CentroidErr
    metrics(end).CellMetrics_TPR_FPR = [CellMetrics.TPR, CellMetrics.FPR]
    metrics(end).CellMetrics_MR = [CellMetrics.MR]
    metrics(end).name = fileName

for i in range(1,len(f2)):
    load([baseDir2, filesep, f2(i).name])
    metrics(end+1).segErrNMap = segErrNMap
    metrics(end).segErrTMap = segErrTMap
    metrics(end).CellMetrics_CentroidErr = CellMetrics.CentroidErr
    metrics(end).CellMetrics_TPR_FPR = [CellMetrics.TPR, CellMetrics.FPR]
    metrics(end).CellMetrics_MR = [CellMetrics.MR]
    metrics(end).name = fileName

for i in range(1,len(f3)):
    load([baseDir3, filesep, f3(i).name])
    metrics(end+1).segErrNMap = segErrNMap
    metrics(end).segErrTMap = segErrTMap
    metrics(end).CellMetrics_CentroidErr = CellMetrics.CentroidErr
    metrics(end).CellMetrics_TPR_FPR = [CellMetrics.TPR, CellMetrics.FPR]
    metrics(end).CellMetrics_MR = [CellMetrics.MR]
    metrics(end).name = fileName

save('metrics_xbrain_run1_2_Nov92015','metrics')

baseDir = '/Users/graywr1/xbrain_hyperparam_rfr/ilastik';
f = dir([baseDir, filesep, '*err*.mat'])

metrics = [];
for i in range(1,len(f)):
    load([baseDir, filesep, f(i).name])
    metrics(end+1).segErrNMap = segErrNMap
    metrics(end).segErrTMap = segErrTMap
    metrics(end).CellMetrics_CentroidErr = CellMetrics.CentroidErr
    metrics(end).CellMetrics_TPR_FPR = [CellMetrics.TPR, CellMetrics.FPR]
    metrics(end).CellMetrics_MR = [CellMetrics.MR]
    metrics(end).name = fileName

save([baseDir, filesep, 'metrics_xbrain_ilastik_rfr_11242015.mat'],'metrics')


baseDir = '/Users/graywr1/xbrain_hyperparam_rfr/gmm'
f = dir([baseDir, filesep, '*err*.mat'])

metrics = []

for i in range(1,len(f)):
    load([baseDir, filesep, f(i).name])
    metrics(end+1).segErrNMap = segErrNMap
    metrics(end).segErrTMap = segErrTMap
    metrics(end).CellMetrics_CentroidErr = CellMetrics.CentroidErr
    metrics(end).CellMetrics_TPR_FPR = [CellMetrics.TPR, CellMetrics.FPR]
    metrics(end).CellMetrics_MR = [CellMetrics.MR]
    metrics(end).name = fileName

save([baseDir, filesep, 'metrics_xbrain_gmm_rfr_11242015.mat'],'metrics')
