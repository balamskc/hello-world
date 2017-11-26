
"""
Created on Tue Oct 24 13:54:55 2017

@author: bgmad1
"""

import pandas as pd
import matplotlib.pyplot as plt

    
import os

import glob
files=[]
file_names=[]
path = '/Users/bgmad1/Documents/cleandata/*.csv'
for filename in glob.glob(path):
    #base=os.path.basename('/Users/bgmad1/Documents/cleandata/trimers.csv')
    base=os.path.basename(filename)
    file_names.append(base)
    #print(base)

    #print(os.path.splitext(base))

    y=os.path.splitext(base)[0]
    print(y)
    x=pd.read_csv((base))
    #print(x.head(2))
    files.append(os.path.splitext(base)[0])
    #df = pd.read_csv('trimer.csv')
    #print(df.head())
    x.columns=['Wavelength','Absorbance(a.u)','l']
    x=x.drop('l',axis=1)
    x = x.apply(pd.to_numeric, errors='coerce')
    x = x.dropna()
    x.to_csv(base,index=False)
    #df2 = pd.read_csv('trimer_clean.csv')
    #print(df2['sample3'][0:3])
    

    x['Wavelength']=x['Wavelength'].round(1)

    maxi=(x['Absorbance(a.u)'].max())
    mini=(x['Absorbance(a.u)'].min())
    x['Norm']=(x['Absorbance(a.u)']-mini)/(maxi-mini)
    A_400=x['Absorbance(a.u)'][x['Wavelength']==400]
    x['A_400']=(x['Absorbance(a.u)']).apply(lambda x: x/A_400)
    plt.plot(x['Wavelength'],x['A_400'],label=y,linewidth=2)
#    plt.plot(x['Wavelength'],x['Absorbance(a.u)'],label=y,linewidth=2)
    #plt.plot(x['Wavelength'],x['Norm'],label=y,linewidth=2)
    #file_name=pd.read_csv(base)


#print([file for file in files])
#print([file_name for file_name in file_names])
plt.axis([350,1000,0,2])
plt.axis('auto')
plt.xlim([300,1000])
plt.legend()
plt.legend(frameon=False)

#plt.title('Gold NP Assembly ')
plt.xlabel('Wavelength (nm)',fontsize=11, fontweight='bold')
plt.ylabel('Absorbance (a.u)',fontsize=11, fontweight='bold')
plt.savefig('blllah.jpg', dpi=2000)      
plt.show()
