import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import datetime as dt
#print("hi")
df1 = pd.read_csv('test_fin.csv')
df = pd.DataFrame(df1)
#print(df.head())
df = df.drop(columns = ['latitude', 'longitude', 'elevation', 'status'])
print(df.head())
new = df.created.str.split(' ', expand = True)
new1 = new[1].str.split(':', expand = True)
#print(new.head())
df['date'] = new[0].copy()
df['time'] = new1[0].astype(str) + ':' + new1[1].astype(str)
print(df.head())
new2 = df.groupby(['time']).mean()
final = new2.copy()
#print(final.head())
final['entry_id'] = final['entry_id'] - 939305
for i in final.columns:
    if i != 'entry_id':
        savename = 'line_plots/line_' + i + '.png'
        #plt.clf()
        line = sns.lineplot(x = 'entry_id', y = i, data = final)
        fig = line.get_figure()
        fig.savefig(savename)
        # save_hist = 'hist_plots/hist_' + i + '.png'
        # #plt.clf()
        # if i == 'Pm10':
        #     plt.xlim(0,200)
        # hist = sns.distplot(final[i])
        # hifig = hist.get_figure()
        # hifig.savefig(save_hist)
