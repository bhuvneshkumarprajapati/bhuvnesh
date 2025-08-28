# lib.py

# This code is used to plot the price and weight of cricket bats using matplotlib and pandas.
'''import matplotlib.pyplot as plt
import pandas as pd
data = {
    "criket_bat":["sg","mrf","ss","gm","kookaburra","puma","adidas","gray_nicolls"],
    "mrp":[1000, 1200, 1500, 1800, 2000, 2200, 2500, 3000],
    "Weight_grams":[1000, 1200, 1500, 1800, 2000, 2200, 2500, 3000],
}
dataFrame = pd.DataFrame(data)
plt.plot(dataFrame["criket_bat"], dataFrame["mrp"], marker='o')
plt.plot(dataFrame["mrp"], dataFrame["Weight_grams"], marker='x')
plt.show()'''


'''import matplotlib.pyplot as plt
import pandas as pd
data = {
    "cricket_bat": ["sg", "mrf", "ss", "gm", "kookaburra", "puma", "adidas", "gray_nicolls"],
    "mrp": [1000, 1200, 1500, 1800, 2000, 2200, 2500, 3000],
    "Weight_grams": [1000, 1200, 1500, 1800, 2000, 2200, 2500, 3000],
}
dataFrame = pd.DataFrame(data)
plt.plot(dataFrame["mrp"], dataFrame["Weight_grams"], marker='o')
plt.xlabel("Price in Rupees")
plt.ylabel("Weight in Grams")
plt.title("Price vs Weight of Cricket Bats")
plt.show()'''


'''import matplotlib.pyplot as plt
import numpy as np
a = np.arange(5)
b = [2, 4, 6, 8, 10]
c = [5, 6, 7, 8, 9]
fig = plt.figure()
ax = plt.subplot()
ax.plot(a, b, 'k--', label = 'Frequency')
ax.plot(a, c, 'k-', label = 'Periods') 
ax.legend()
plt.title("Frequency of a signal")
plt.show()'''




'''import matplotlib.pyplot as plt
import numpy as np
a = np.arange(5)
b = [2, 4, 6, 8, 10]
c = [5, 6, 7, 8, 9]
fig = plt.figure()
ax = plt.subplot()
ax.plot(a, b, 'k--', label='Frequency')
ax.plot(a, c, 'k:', label='Period')
ax.legend(loc = "upper center")
plt.title("Frequency of a Signal")
plt.show()'''



'''import matplotlib.pyplot as plt
import numpy as np
a = np.arange(5)
b = [2, 4, 6, 8, 10]
c = [5, 6, 7, 8, 9]
fig = plt.figure()
ax = plt.subplot()
ax.plot(a, b, 'k--', label = 'Frequency')
ax.plot(a, c, 'k:', label = 'Period')
legend = ax.legend(loc = 'upper center')
legend.get_frame().set_facecolor('lightblue')
plt.title("Frequency of a Signal")
plt.show()'''



'''import matplotlib.pyplot as plt
import numpy as np
a = np.arange(5)
b = [2, 4, 6, 8, 10]
c = [5, 6, 7, 8, 9]
fig = plt.figure()
ax = plt.subplot()
ax.plot(a, b, 'k--', label = 'Frequency')
ax.plot(a, c, 'k:', label = 'Periods')
ax.legend(loc = 'upper center', fontsize = 'xx-large')
plt.title("Frequency of a Signal", fontsize = 'xx-large', color = 'blue')
plt.show()'''




'''import matplotlib.pyplot as plt
import numpy as np
student = np.array(["raja", "bhanu", "kanishka", "priyanshi", "poorvi", "virat"])
marks = np.array([85, 52, 95, 86, 74, 65])
plt.bar(student, marks)
plt.xlabel("student")
plt.ylabel("marks")
plt.title("student marks")
plt.show()'''


'''import matplotlib.pyplot as plt
import numpy as np
player = np.array(["Raja", "kanishka", "Siya", "Poorvi", "Manvi"])
score = np.array([85, 98, 52, 86, 99])
plt.pie(score, labels = player, autopct = '%1.2f%%')
plt.title("Player score")
plt.show()'''


'''import matplotlib.pyplot as plt
import numpy as np
months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "june", "Jul", "Aug", "Sep", "OCt", "Nov", "Dec"])
rain  = np.array([60, 50, 20, 59, 87, 56, 78, 54, 74, 89, 78, 74])
plt.plot(months, rain)
plt.xlabel("months")
plt.ylabel("rain")
plt.title("Rain Fall in Year")
plt.show()'''


'''import matplotlib.pyplot as plt
import numpy as  np
arr = np.array([10, 52, 58, 89, 56, 78, 89, 81, 99, 83, 14, 25, 89, 68, 97,96])
plt.hist(arr, bins = [0, 20, 40, 60, 80, 100])
plt.xlabel("marks")
plt.ylabel("student")
plt.title("student  marks")
plt.show()'''


 
