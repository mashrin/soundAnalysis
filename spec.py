import glob
import os
import librosa
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import specgram
#%matplotlib inline
plt.style.use('classic')

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Ubuntu'
plt.rcParams['font.monospace'] = 'Ubuntu Mono'
plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 11
plt.rcParams['figure.titlesize'] = 13
def plot_specgram():
    i=[1,1,1,1,1,1,1,1,1,1]
#    sub_dirs = ['fold1','fold2','fold3','fold4','fold5','fold6','fold7','fold8','fold9','fold10']
    sub_dirs = ['fold41']
    for label, sub_dir in enumerate(sub_dirs):
        for fil in os.listdir(sub_dir):
            fil1=os.path.join(sub_dir,fil)
            fig = plt.figure(figsize=(60,30), dpi = 300)
            X,sr = librosa.load(fil1)
            label = int(fil.split('-')[1]) 
            specgram(np.array(X), Fs=22050)
            fig.savefig('i'+str(label+1)+'/'+str(label+1)+'_'+str(i[label])+'.png')   # save the figure to file
            i[label]=i[label]+1
            plt.close()
plot_specgram()
plt.show()
