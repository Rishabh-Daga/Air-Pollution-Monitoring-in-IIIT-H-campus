import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import datetime as dt
#print("hi")
df1 = pd.read_csv('week_data_test/final1_1.csv')
df = pd.DataFrame(df1)
#print(df.head())
df = df.drop(columns = ['latitude', 'longitude', 'elevation', 'status'])
df=df.rename(columns={'field1' : 'Temperature' ,'field2' : 'Humidity' , 'field3' : 'Pm2.5','field4':'Pm10','field5' : 'CO','field6':'NO2','field7' : 'NH3' })
#print(df.head())
new = df.created_at.str.split(' ', expand = True)
new1 = new[1].str.split(':', expand = True)
df['date'] = new[0].copy()
print(new.head())
df['time'] = new1[0].astype(str)
#print(df.head())
new2 = df.groupby(['time']).mean()
final = new2.copy()
#print(final.head())
final['entry_id'] = final['entry_id'] - 939305
for i in final.columns:
    if i != 'entry_id':
        savename = 'line_plots_week/line_1_1' + i + '.png'
        plt.clf()
        line = sns.lineplot(x = 'entry_id', y = i, data = final)
        fig = line.get_figure()
        fig.savefig(savename)
        save_hist = 'hist_plots_week/hist_1_1' + i + '.png'
        plt.clf()
        if i == 'Pm10':
            plt.xlim(0,200)
        hist = sns.distplot(final[i])
        hifig = hist.get_figure()
        hifig.savefig(save_hist)
