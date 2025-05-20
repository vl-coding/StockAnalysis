# --- read a file to obatin a list of numbers ------
import csv

file_path = "Project-1/project-1.csv"

def read_file(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        spy = []
        for row in csv_reader:
                spy.append(row[1])

    return list(map(float, spy)) 
    
spy = read_file(file_path)
# print(spy)

# ---------------------------------------------------
# A. Define a rising day as 
#    the day when the closing price is higher than the previous day

# I. Obtain the number of rising days from 1/2/2024 through 6/28/2024
#    Print out the number of rising days
def num_rise_days(l):
    rising = 0
    for i in range(len(l)):
        if i == 0:
            continue
        if l[i] > l[i - 1]:
            rising += 1
    return rising
print(f"The number of rising days from 1/2/2024 through 6/28/2024:\n{num_rise_days(spy)}\n")

# II. How many days did the rise last at most?
def rise_last(l):
    rising = 0
    max = 0
    for i in range(len(l)):
        if(i == 0):
            continue
        if(l[i] > l[i-1]):
            rising += 1
            if(rising > max):
                max = rising
        else:
            rising = 0
    return max
print(f"The number of days the rise lasted at most:\n{rise_last(spy)}\n")

# ---------------------------------------------------
# B. Moving Averages (MA) are the means for sequences of consecutive time-series values 
#    for a time duration L
#    For example, given the daily values, 10, 9, 11, 12, 19, the 3-day moving averages 
#    are 10.00, 10.67, and 14.00, where the first MA value, 10.00, 
#    is the mean of the first three values (10, 9, and 11) and so on so forth

# I. (5 pts) Try to calculate 5-day moving averages.
def moving_avg(l, t):
    rst = []
    for i in range(len(l)):
        if(i in range(t-1)):
            continue
        ma = sum(l[i-(t-1):i+1]) / t
        rst.append(ma)
    return rst
ma_5d = moving_avg(spy, 5)

# II. (3 pts) Obtain the number of rising days in the 5-day moving averages.
print(f"The number of rising days in the 5-day moving averages:\n{num_rise_days(ma_5d)}\n")

# III. (8 pts) How many days did the 5-day moving averages rise last at most?
print(f"The days the 5-day moving averages rise lasted at most:\n{rise_last(ma_5d)}\n")

# IV. (5 pts) How many days were the SPY closing prices lower than 
# the 5-day moving averages.
def less_ma(l, t):
    ma_l = moving_avg(l, t)
    count = 0 
    for i in range(len(ma_l)):
        if(l[i+(t-1)] < ma_l[i]):
            count += 1
    return count
print(f"The days the SPY closing prices were lower than the 5-day moving averages:\n{less_ma(spy, 5)}\n")