import os

files = os.listdir('.')

for file in files:
    if file.endswith('.png'):
        old = file.split('_')
        temp = old[2].split('.')
        old[1] = old[1].replace('n', '')
#        print(old[1] + ' ' + temp[0])
        new = old[0] + '_' + old[1] + '_day_' + temp[0] + '.png'
        os.rename(file, new)
