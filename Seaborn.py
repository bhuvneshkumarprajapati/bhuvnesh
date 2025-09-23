# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# var = [1,2,3,4,5,6,7]
# var_1 = [2,3,4,5,6,7,8]
# x_1 = pd.DataFrame({'var':var, 'var_1':var_1})
# sns.lineplot(x = 'var', y = 'var_1', data = x_1)
# plt.grid()
# plt.title("Line Plot")
# plt.show()  




# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# name = ["Raja","Rani","Rahul","Rohit","Rajesh"]
# marks = [98,94,45,65,78]
# y_1 = pd.DataFrame({'name':name, 'marks':marks})
# sns.barplot(x = name, y = marks, data = y_1)
# plt.show()



# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# players = ["Rohit","Virat","Dhoni","Raina","Jadeja"]
# score = [120,150,90,80,70]
# x_1 = pd.DataFrame({'players':players, 'score':score})
# sns.lineplot(x = 'players', y = 'score', data = x_1)
# plt.grid()
# plt.title("Cicket Players score")
# plt.show()


# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# var = sns.load_dataset("exercise")
# print(var) 
# sns.barplot(x = var.time, y = var.pulse, data = var, palette="mako", orient='v',saturation=1, alpha=0.9)
# plt.title("Time  vs diet")
# plt.show()



#kde = kernel density estimation
# import seaborn as sns
# import  matplotlib.pyplot as plt
# import pandas as pd
# var = sns.load_dataset("exercise")
# print(var)
# sns.displot(var['diet'],bins = [170 ,180,190,200,210,220,230,240,250], color="r", kde = True , rug = True, log_scale=True)
# plt.show()




# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# var = sns.load_dataset("exercise")
# sns.scatterplot(x = var.id, y = var.pulse, data = var, color = "g", marker = "o", s = 100, hue = var.diet, style=var.diet, size = var.diet,sizes = [50,200],alpha=0.9)
# plt.title("time vs diet")




