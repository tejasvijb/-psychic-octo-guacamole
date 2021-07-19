import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Attendance.csv')

count = 1
names = []
for name in df['Name'].unique():
    print(count,name)
    names.append(name)
    count += 1

name = int(input('\nSelect a student : '))
name = name - 1

  
dfteja = df[df['Name']==names[name]]

dfteja = dfteja[['Name','Subject']]

newdf = pd.DataFrame(dfteja.value_counts())
x = np.array(newdf.index.get_level_values(1))
y = np.array(newdf.iloc[:,0])
fig = plt.figure(figsize = (10, 10))
plt.xlabel("Subjects")
plt.ylabel("No. of days present")
title = "Attendance of" + " " + names[name]
plt.title(title)
plt.grid(True, color = "grey", linewidth = "0.5", linestyle = "-")
plt.bar(x, y,width = 0.3)   
plt.show()

print('\n')
print(pd.DataFrame(dfteja.value_counts()))    