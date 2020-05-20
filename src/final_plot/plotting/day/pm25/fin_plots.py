import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import datetime as dt
from os import listdir

# df = pd.read_csv('comtemp.csv')
# # `line` = sns.lineplot(x = 'timestamp', y = 'temp', data=df)
# n = 24
# line = sns.barplot(x = 'timestamp', y = 'value', hue='variable', data=pd.melt(df, ['timestamp']    ))
# # sns.set(font_scale=2)
# # [l = l.split(" ").join("\n") for (i,l) in enumerate(line.get_xticklabels()) if i % n == 0]
# k = 21
# # [l.set_visible(False) for (i,l) in enumerate(line.get_xticklabels()) if i % n != 0]
# labels = [i.get_text() for i in line.get_xticklabels()]
# for i in range(len(labels)):
#     labels[i] = str(k) + "-02"
#     print(str(k) + " " + str(i) + " " + labels[i])
#     if i % n == 0:
#         k += 1
#     i *= 24
# line.set_xticklabels(labels)
# plt.ylim(15,60)
# line.set(xlabel='Date', ylabel='temp')
# [l.set_visible(False) for (i,l) in enumerate(line.get_xticklabels()) if i % n != 0]
# # plt.rcParams['title.fontsize'] = 8
# plt.rcParams['legend.fontsize'] = 8
# # line.set_xticklabels(['21-02', '22-02', '23-02', '24-02', '25-02', '26-02', '27-02', '28-02'])
# fig = line.get_figure()
# fig.savefig('hourly_temp.png')
translate = {'n11': 'Faculty Quarters', 'n12' : 'Library', 'n14' : 'Main Gate', 'n24' : 'KCIS', 'n31' : 'OBH', 'n32' : 'Felicity Ground', 'n33' : 'Bakul Niwas'}

for i in listdir('./'):
    if i.endswith(".csv"):
        print(i)
        plt.clf()
        temp = i
        tok = temp.split('_')[1]
        day = temp.split("_")[2].split('.')[0]
        df = pd.read_csv(i)
        df.rename(columns = translate, inplace = True)
        plt.clf()
        grid, ax = plt.subplots(figsize=(20,8))
        n = 24
        line = sns.lineplot(x = 'timestamp', y = 'value', hue = 'variable', data=pd.melt(df, ['timestamp']))
        k = 22
        line.axes.set_title('One week data for ' + tok, fontsize = 30)
        labels = [i.get_text() for i in line.get_xticklabels()]
        for i in range(len(labels)):
            labels[i] = str(k) + "-02"
            # print(str(k) + " " + str(i) + " " + labels[i])
            if i % n == 0:
                k += 1
                i *= 24
        line.set_xticklabels(labels)
        line.set_xlabel('Date', size =18)
        line.set_ylabel(tok, size = 18)
        if tok == 'temp':
            line.set_ylabel(tok + '( degree C )', size = 18)
            plt.ylim(15,50)
        elif tok == 'humidity':
            line.set_ylabel(tok + '( % )', size = 18)
            plt.ylim(0,100)
        elif tok == 'pm25':
            line.set_ylabel(tok + '( ppm )', size = 18)
            plt.ylim(0, 100)
        elif tok == 'pm10':
            line.set_ylabel(tok + '( ppm )', size = 18)
            plt.ylim(0, 140)
        # line.set(xlabel='Date', ylabel=tok)
       
        [l.set_visible(False) for (i,l) in enumerate(line.get_xticklabels()) if i % n != 0]
        savename = './plots/' + tok + '_all_day_' + day + '.png'
        week = line.get_figure()
        week.savefig(savename, pad_inches=0, bbox_inches='tight')
        plt.close()
        for col in df.columns:
            print(col)
            if col != 'timestamp':
                plt.clf()
                grid, ax = plt.subplots(figsize=(20,8))
                # sns.set(rc={'figure.figsize':(11.7,8.27)})
                line.axes.set_title('One day data for ' + tok, fontsize = 30)
                n = 60
                line = sns.lineplot(x = 'timestamp', y = col, data=df)
                # sns.set(font_scale=2)
                # [l = l.split(" ").join("\n") for (i,l) in enumerate(line.get_xticklabels()) if i % n == 0]
                k = 0
                # plt.rcParams['legend.fontsize'] = 8
                # plt.rcParams['figure.figsize'] = 16, 9
                # line.set_size_inches(10.0, 5.0)
                # [l.set_visible(False) for (i,l) in enumerate(line.get_xticklabels()) if i % n != 0]
                labels = [i.get_text() for i in line.get_xticklabels()]
                for i in range(len(labels)):
                    labels[i] = str(k) + ":00"
                    # print(str(k) + " " + str(i) + " " + labels[i])
                    if i % n == 0:
                        k += 2
                    i *= 60
                line.set_xticklabels(labels)
                line.set_xlabel('Date', size =18)
                line.set_ylabel(tok, size = 18)
                if tok == 'temp':
                    line.set_ylabel(tok + '( degree C )', size = 18)
                    plt.ylim(15,50)
                elif tok == 'humidity':
                    line.set_ylabel(tok + '( % )', size = 18)
                    plt.ylim(0,100)
                elif tok == 'pm25':
                    line.set_ylabel(tok + '( ppm )', size = 18)
                    plt.ylim(0, 100)
                elif tok == 'pm10':
                    line.set_ylabel(tok + '( ppm )', size = 18)
                    plt.ylim(0, 140)
                [l.set_visible(False) for (i,l) in enumerate(line.get_xticklabels()) if i % n != 0]
                # plt.rcParams['title.fontsize'] = 8
                # plt.rcParams['legend.fontsize'] = 8
                # plt.rcParams['figure.figsize'] = 16, 9
                # line.set_xticklabels(['21-02', '22-02', '23-02', '24-02', '25-02', '26-02', '27-02', '28-02'])
                fig = line.get_figure()
                saver = list(translate.keys())[list(translate.values()).index(col)]
                saver = saver.replace('n', '')
                savename="./plots/" + tok + "_" + saver + "_day_" + day + ".png"
                fig.savefig(savename, pad_inches = 0, bbox_inches = 'tight')
                plt.close()
                plt.clf()
                grid, ax = plt.subplots(figsize=(20,8))
                hist = sns.distplot(df[col], bins = 20)
                hist.axes.set_title('One week data for ' + tok, fontsize = 30)
                if tok == 'temp':
                    hist.set_xlabel(col + '( degree C )', size = 18)
                    # plt.ylim(15,50)
                elif tok == 'humidity':
                    hist.set_xlabel(col + '( % )', size = 18)
                    # plt.ylim(0,100)
                elif tok == 'pm25':
                    hist.set_xlabel(col + '( ppm )', size = 18)
                    # plt.ylim(0, 100)
                elif tok == 'pm10':
                    hist.set_xlabel(col + '( ppm )', size = 18)
                    # plt.ylim(0, 140)
                hist.set_ylabel('Distribution', size =18)
                if tok == 'pm10':
                    plt.xlim(0,140)
                elif tok == 'humidity':
                    plt.xlim(10,100)
                ter = list(translate.keys())[list(translate.values()).index(col)]
                ter = ter.replace('n', '')
                savehist = "./hist/" + tok + "_" + ter + "_day_" + day + ".png"
                saver = hist.get_figure()
                saver.savefig(savehist, pad_inches = 0, bbox_inches = 'tight')
                plt.close()
