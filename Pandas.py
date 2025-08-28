# import pandas as  pd
# data={
#     'Student':["John", "Alice", "Bob", "Diana"],
#     'Rank': [1, 2, 3, 4],
#     'marks': [85, 90, 78, 88]
# }
# df=pd.DataFrame(data)
# print(df)


# import pandas as pd
# data = {
#     'Student': ["John", "Alice", "Bob", "Diana"],
#     'Rank': [1, 2, 3, 4],
#     'marks': [85, 90, 78, 88]
# }
# df=pd.DataFrame(data, index=['RowA', 'RowB', 'RowC', 'RowD' ])
# print(df)


# import pandas as pd
# data = {
#     'Student': ["John", "Alice", "Bob", "Diana"],
#     'Rank': [1, 2, 3, 4],
#     'marks': [85, 90, 78, 88]
# }
# df=pd.DataFrame(data, index = ['student1', 'student2', 'student3', 'student4'])
# print(df)
# for col in df:
#     print(col)



# import pandas as pd
# data={
#     'Student': ["John", "Alice", "Bob", "Diana"],
#     'Rank': [1, 2, 3, 4],
#     'marks': [85, 90, 78, 88]
# }
# df=pd.DataFrame(data, index=['RowA', 'RowB', 'RowC', 'RowD'])
# print(df)
# print(df.dtypes)


# import pandas as pd
# data = {
#     'Student': ["John", "Alice", "Bob", "Diana"],
#     'Rank': [1, 2, 3, 4],
#     'marks': [85, 90, 78, 88]
# }
# df = pd.DataFrame(data, index=['RowA', 'RowB', 'RowC', 'RowD'])
# print(df)
# print(df.ndim)


# import pandas as pd
# data = {
#     'Student': ["John", "Alice", "Bob", "Diana"],
#     'Rank': [1, 2, 3, 4],
#     'marks': [85, 90, 78, 88]
# }
# df = pd.DataFrame(data, index=['RowA', 'RowB', 'RowC', 'RowD'])
# print(df)
# print(df.size)


# import pandas as pd
# data = {
#     'Student': ["John", "Alice", "Bob", "Diana"],
#     'Rank': [1, 2, 3, 4],
#     'marks': [85, 90, 78, 88]
# }
# df = pd.DataFrame(data, index=['RowA', 'RowB', 'RowC', 'RowD'] )
# print(df)
# print(df.shape)


# import pandas as pd
# data = {
#     'Student': ["John", "Alice", "Bob", "Diana"],
#     'Rank': [1, 2, 3, 4],
#     'marks': [85, 90, 78, 88]
# }
# df = pd.DataFrame(data, index=['RowA', 'RowB', 'RowC', 'RowD'])
# print(df)
# print(df.index)



# import pandas as pd
# data = {
#     'Student': ["John", "Alice", "Bob", "Diana"],
#     'Rank': [1, 2, 3, 4],
#     'marks': [85, 90, 78, 88]
# }
# df = pd.DataFrame(data, index=['RowA', 'RowB', 'RowC', 'RowD'])
# print(df)
# print(df.T)


# import pandas as pd
# data = {
#     'Student': ["John", "Alice", "Bob", "Diana"],
#     'Rank': [1, 2, 3, 4],
#     'marks': [85, 90, 78, 88]
# }
# df = pd.DataFrame(data, index=['RowA', 'RowB', 'RowC', 'RowD'])
# print(df)
# print(df.head(2))
# print(df.tail(2))


# import pandas as pd
# data1 = {
#     'id' : ["S01", "S02", "S03", "S04"],
#     'student' : ["John", "Alice", "Bob", "Diana"],
#     'roll_no' : [101, 102, 103, 104],

# }
# data2 = {
#     'rank' : [1, 2, 3, 4],
#     'marks' : [85, 90, 78, 88],
# }
# df1 = pd.DataFrame(data1)
# df2 = pd.DataFrame(data2)
# print(df1)
# print(df2)
# resDF = df1.join(df2)
# print(resDF)


# import pandas as pd
# data1 = {
#     'id': ["S01", "S02", "S03", "S04"],
#     'student': ["John", "Alice", "Bob", "Diana"],
#     'roll_no': [101, 102, 103, 104],
# }
# data2 = {
#     'rank': [1, 2, 3, 4],
#     'marks': [85, 90, 78, 88],
# }
# df1 = pd.DataFrame(data1, index = ['RowA', 'RowB', 'RowC', 'RowD'])
# df2 = pd.DataFrame(data2, index = ['RowE', 'RowF', 'RowG', 'RowH'])
# print(df1)
# print(df2)
# resdf = pd.concat([df1, df2], axis=1)
# print(resdf)



# import pandas as pd
# data = [10,20,30,40,50]
# s = pd.Series(data)
# print(s[2])


# import pandas as pd 
# data = [50,89,23,69,78,45]
# sr = pd.Series(data)
# print(sr)



# import pandas as pd
# data = [10,20,30,40,50]
# sr = pd.Series(data,index = ["RowA","RowB","RowC","RowD","RowE"])
# print(sr)
# print(sr["RowD"])



# import pandas as pd
# data = [10,20,40,80,100]
# s = pd.Series(data)
# print(s)
# print(s.dtype)


# import pandas as pd
# data = [100,60,80,90,70,30]
# sr = pd.Series(data)
# print(sr)
# print(sr.ndim)



# import pandas as pd
# data = [50,60,89,78,52]
# sr = pd.Series(data)
# print(sr)
# print(sr.size)



# import pandas as pd
# data = [52,64,89,47,16,68]
# sr = pd.Series(data)
# print(sr)
# print(sr.name)


# import pandas as pd
# data = [10,20,50,62,83,62,96]
# sr = pd.Series(data)
# print(data)
# print(sr.hasnans)



# import pandas as pd
# data = [89,56,23,78]
# sr = pd.Series(data)
# print(sr)
# print(sr.hasnans)


# import pandas as pd
# data = [1,2,3,4,5]
# sr = pd.Series(data)
# print(sr)
# print(sr.index)

#head function is ysed for return first n rows
# import pandas as pd
# data = [25,35,45,55,65,75]
# sr = pd.Series(data)
# print(sr)
# print(sr.head(2))


#tail  functiobn is used for return laast n rows
# import pandas as pd
# data = [23,85,68,98,77,45]
# sr = pd.Series(data)
# print(sr)
# print(sr.tail(2))



# import pandas as pd
# data = [12,56,48,75,96]
# sr = pd.Series(data, index = ["NUM1","NUM2","NUM3","NUM4","NUM5"])
# print(sr)
# print(sr.info())



# import pandas as pd
# data1 = [10,20,30,40,50]
# data2 = [25,35,64,89,85]
# sr1 = pd.Series(data1)
# sr2 = pd.Series(data2)
# print(sr1)
# print(sr2)
# def demo(x1,x2):
#     if(x1>x2):
#         return x1
#     else:
#         return x2
# res = sr1.combine(sr2,demo)
# print(res)


#CAtegorical data takes limitted no of possible vlaues

# import pandas as pd
# s = pds.Series(["p","q","r","s","q"],dtype = "category")
# print(s)


# import pandas as pd
# s = pd.Series(["p","q","r","s"], dtype = "category")
# print(s)
# s = s.cat.add_categories("t")
# print(s)



# import pandas as pd
# s = pd.Series(["p","q","r","s"], dtype = "category")
# s = s.cat.remove_categories("r")
# print(s)


# import pandas as pd
# df = pd.read_csv("path of the csv ")
# print(df)


# import pandas as pd
# data = {
#     'Student':["Amit","Raja","Prince","Divya","Alkusha"],
#     'Rank':[1,4,3,2,5],
#     'Marks':[98,95,64,32,26]
# }
# df = pd.DataFrame(data)
# print(df[['Rank',"Marks"]])



# import pandas as pd
# data = {
#     'Id':["S01","S02","S03","S04","S05"],
#     'Student':["AMit","Chutiya","Hitten","Bhadwa","Surya"],
#     'Roll':[101,102,103,104,105],
#     'Rank':[1,4,3,2,5],
#     'Marks':[98,95,66,45,20],
#     'Address':["East","West","North","south","SouthWest"]
# }
# df = pd.DataFrame(data)
# print(df)
# print(df[df.columns[2:5]])


# import pandas as pd
# data = {
#     'Id':["S01","S02","S03","S04","S05"],
#     'Student':["AMit","Chutiya","Hitten","Bhadwa","Surya"],
#     'Rank':[1,4,3,2,5],
#     'Marks':[98,95,66,45,20]
# }
# df = pd.DataFrame(data)
# df.insert(2, "Rollno",[101,102,103,104,105])
# print(df)


# import pandas as pd
# data = {
#     'Id':["S01","S02","S03","S04","S05"],
#     'Student':["AMit","Chutiya","Hitten","Bhadwa","Surya"],
#     'Rank':[1,4,3,2,5],
#     'Marks':[98,95,66,45,20]
# }
# df = pd.DataFrame(data)
# resdf = df.assign(Rollno=[101,102,103,104,105])
# print(resdf)


# import pandas as pd
# data = {
#     'Id':["S01","S02","S03","S04","S05"],
#     'Student':["AMit","Chutiya","Hitten","Bhadwa","Surya"],
#     'Rank':[1,4,3,2,5],
#     'Marks':[98,95,66,45,20]
# }
# df = pd.DataFrame(data)
# print(df)
# resdf = df.drop("Marks",axis = 1)
# print(resdf)



# import pandas as pd
# data = {
#     'Id':["S01","S02","S03","S04","S05"],
#     'Student':["AMit","Chutiya","Hitten","Bhadwa","Surya"],
#     'Rank':[1,4,3,2,5],
#     'Marks':[98,95,66,45,20]
# }
# df = pd.DataFrame(data)
# print(df)
# resdf = df.drop(2,axis = 'index')
# print(resdf)


# import pandas as pd
# data = {
#     'Id':["S01","S02","S03","S04","S05"],
#     'Student':["AMit","Chutiya","Hitten","Bhadwa","Surya"],
#     'Rank':[1,4,3,2,5]
# }
# df = pd.DataFrame(data)
# print(df)
# for row in df.iterrows():
#     print(row)



# import pandas as pd
# data = {
#     'Id':["S01","S02","S03","S04","S05"],
#     'Student':["AMit","Chutiya","Hitten","Bhadwa","Surya"],
#     'Rank':[1,4,3,2,5]
# }
# df = pd.DataFrame(data)
# print(df)
# for row in df.itertuples():
#     print(row)



# import pandas as pd
# data = {
#     'Student':(["AMit","Chutiya","Hitten","Bhadwa","Surya"]),
#     'Rank':[1,4,3,2,5],
#     'Marks':[98,95,66,45,20]
# }
# df = pd.DataFrame(data,index=["RowA","RowB","RowC","RowD","RowE"])
# print(df)
# print(df.sort_values(by=['Rank']))



# import  pandas as pd
# data = {
#     'student':["Amit","Raja","Adarsh","Poorvi","Rems"],
#     'Rank':[1,2,3,4,5],
#     'MArks':[98,96,23,45,65]
# }
# df = pd.DataFrame(data)
# print(df.duplicated())




# import pandas as pd
# data = {
#     'student':["Amit","Raja","Amit","Poorvi","Rems"],
#     'Rank':[1,2,1,4,5],
#     'MArks':[98,96,98,45,65]
# }
# df = pd.DataFrame(data)
# resdf = df.drop_duplicates()
# print(resdf)



# import pandas as pd
# data = ["Raja","Yashu","BHANU","PRiYansHi","YArraA"]
# sr = pd.Series(data)
# print(sr)
# print(sr.str.lower())



# import pandas as pd
# data = ["Raja","Yashu","BHANU","PRiYansHi","YArraA"]
# sr = pd.Series(data)
# print(sr)
# print(sr.str.upper())




# import pandas as pd
# data = ["Raja","Yashu","BHANU","PRiYansHi","YArraA"]
# sr = pd.Series(data)
# print(sr)
# print(sr.str.title())




# import pandas as pd 
# data  = ["Raja","Yashu","BHANU","PRiYansHi","YArraA"]
# sr = pd.Series(data)
# print(sr)
# print(sr.str.len())



# import pandas as pd
# data = ["Raja","Yashu","BHANU","PRiYansHi","YArraA"]
# sr = pd.Series(data)
# print(sr)
# print(sr.count())



# import pandas as pd
# data = ["Raja","Yashu","BHANU","PRiYansHi","YArraA"]
# sr =  pd.Series(data)
# print(sr)
# print(sr.str.contains("Raja"))


 
# import pandas as pd
# print(pd.Timestamp.now())


# import pandas as pd
# time = pd.Timestamp(year=2023, month=8, day=11, hour = 12)
# print(time)
# print(time.dayofweek)
# print(time.dayofyear)
# print(time.daysinmonth)
# print(time.is_leap_year)


#strip,lstrip,rstrip

# import pandas as pd
# data  = ["Jacob",    "raja", "Sanjan", "rampal"]
# sr = pd.Series(data)
# print(sr.str.strip())


# import pandas as pd
# data = {
#     'Player':["Amit","John","Raja","Bhanu"] ,   
#     'Rank':[1,4,3,2],
#     'Year':[2023,2024,2025,2021]
# }
# df  = pd.DataFrame(data)
# res = df.groupby('Player')
# print(res.first())



# import pandas as pd
# import matplotlib.pyplot as plt
# data = {
#     "Temperature": [18,20,12,56,58,41],
#     "Humidity": [32,51,30,56,81,89],
#     "Wind": [12,20,9,8,45,65],
#     "Precipitation":[17,25,89,74,14,52]
# }
# df = pd.DataFrame(data)
# df.plot()
# plt.show()




# import pandas as pd
# import matplotlib.pyplot as plt
# data = {
#     "Temperature": [18,20,12,56,58,41],
#     "Humidity": [32,51,30,56,81,89],
#     "Wind": [12,20,9,8,45,65],
#     "Precipitation":[17,25,89,74,14,52]
# }
# df = pd.DataFrame(data)
# df["Humidity"].plot(kind = "hist")
# plt.show()



