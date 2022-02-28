import random
from itertools import count
import json
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
#https://stackoverflow.com/questions/13942956/disable-matplotlib-toolbar
plt.rcParams['toolbar'] = 'None'
f = open('joe1.json',)

# returns JSON object as a dictionary
data = json.load(f)
 
# Iterating through the json list
f.close()

x_vals = []
y_vals = []

fig, (ax1,ax2) = plt.subplots(nrows=2,ncols=1)

#https://www.youtube.com/watch?v=XFZRVnP-MTU
#https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/Matplotlib/09-LiveData/starting_code.py
index = count()
print(len(data['ch1']))
def animate(i):
    #stops function if window closes.
    #https://stackoverflow.com/questions/7557098/matplotlib-interactive-mode-determine-if-figure-window-is-still-displayed
    if not plt.get_fignums():
        return
    x_vals.append(next(index)//2)
    print(len(x_vals))
    if len(x_vals) > 128:
        x_vals.pop(0)
        y_vals.pop(0)
    y_vals.append(data['ch1'][next(index)%256])
    ax1.cla()
    ax1.plot(x_vals, y_vals)
    ax2.cla()
    ax2.plot(x_vals, y_vals)
    plt.pause(0.1)

#repeats as more values are added indefinitely
ani = FuncAnimation(plt.gcf(), animate, interval=10)

#ax2.specgram()
#ax2.colorbar()

plt.tight_layout()
plt.show()
