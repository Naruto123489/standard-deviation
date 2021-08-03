import math

# list of elements to calculate mean
import csv
with open('class.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

#sorting the data to get the list
data = file_data[0]


# finding mean
def mean(data):
    n= len(data)
    total =0
    for x in data:
        total += int(x)

    mean = total / n
    return mean

#Subtract the mean from  the values and square them
squared_list= []
for number in data:
    a = int(number) - mean(data)
    a= a**2
    squared_list.append(a)

#Get the sum of all the elements from the squared list
sum =0
for i in squared_list:
 sum =sum + i #sum += i

#Divide the sum by the number of values in the dataset
result = sum/(len(data)-1)

#get the square root of the result
std_deviation = math.sqrt(result)

print(std_deviation)
