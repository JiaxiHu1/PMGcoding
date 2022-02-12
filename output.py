
import csv 
'''
import pandas as pd 
import os 
'''
# I haven't learned how to import pandas and I tried search on google. it didnt work out 
# so I manually add another column as their file name 


#open who files and one for append and one to read 
file1 = open('accessories.csv','r')

stdout = csv.reader(file1,delimiter=',')

outfile = open('stdout.csv','w')


for record in stdout:
    outfile.write(record[0]+','+record[1]+','+'accessories.csv'+'\n')

#this is the end of the first file - accessories file 

file2 = open('clothing.csv','r')
stdout2 = csv.reader(file2,delimiter=',')

outfile = open("stdout.csv",'a')

for record in stdout2:
    outfile.write(record[0]+','+record[1]+','+"clothing.csv"+'\n')

#this is the end of the second file - clothing file 

file3 = open('household_cleaners.csv','r')
stdout3 = csv.reader(file3,delimiter=',')

outfile = open("stdout.csv",'a')

for record in stdout3:
    outfile.write(record[0]+','+record[1]+','+"household_cleaners.csv"+'\n')

outfile.close()

'''
df = pd.read_csv("stdout.csv")
df["filename"] = "accessories.csv"
df.to_csv("stdout.csv", index = False)
'''

