from os import stat
import pandas as pd
import statistics
import csv

df = pd.read_csv("data.csv")
height_list = df["Height(Inches)"].tolist()
weight_list =  df["Weight(Pounds)"].tolist()

height_mean = statistics.mean(height_list)
weight_mean = statistics.mean(weight_list)
print("The mean of height and weight is", height_mean, weight_mean)

height_median = statistics.median(height_list)
weight_median = statistics.median(weight_list)
print("The median of height and weight is", height_median, weight_median)

height_mode = statistics.mode(height_list)
weight_mode = statistics.mode(weight_list)
print("The mode of height and weight is", height_mode, weight_mode)

height_std = statistics.stdev(height_list)
weight_std = statistics.stdev(weight_list)
print("The standard deviation of height and weight is", height_std, weight_std)

first_height_std_start, first_height_std_end = height_mean - height_std, height_mean + height_std
height_list_1_std = [result for result in height_list if result > height_mean - height_std and result < height_mean + height_std] 
print("The percentage of height data lies within the first standard deviation is", len(height_list_1_std) * 100.0 /len(height_list))

second_height_std_start, second_height_std_end = height_mean - (2*height_std), height_mean + 2*height_std
height_list_2_std = [result for result in height_list if result > height_mean - 2*height_std and result < height_mean + 2*height_std] 
print("The percentage of height data lies within the second standard deviation is", len(height_list_2_std) * 100.0 /len(height_list))

third_height_std_start, third_height_std_end = height_mean - 3*height_std, height_mean + 3*height_std
height_list_3_std = [result for result in height_list if result > height_mean - 3*height_std and result < height_mean + 3*height_std] 
print("The percentage of height data lies within the third standard deviation is", len(height_list_3_std) * 100.0 /len(height_list))

first_weight_std_start, first_weight_std_end = weight_mean - weight_std, weight_mean + weight_std
weight_list_1_std = [result for result in weight_list if result > weight_mean - weight_std and result < weight_mean + weight_std] 
print("The percentage of weight data lies within the first standard deviation is", len(weight_list_1_std) * 100.0 /len(weight_list))

second_weight_std_start, second_weight_std_end = weight_mean - (2*weight_std), weight_mean + 2*weight_std
weight_list_2_std = [result for result in weight_list if result > weight_mean - 2*weight_std and result < weight_mean + 2*weight_std] 
print("The percentage of weight data lies within the second standard deviation is", len(weight_list_2_std) * 100.0 /len(weight_list))

third_weight_std_start, third_weight_std_end = weight_mean - 3*weight_std, weight_mean + 3*weight_std
weight_list_3_std = [result for result in weight_list if result > weight_mean - 3*weight_std and result < weight_mean + 3*weight_std] 
print("The percentage of weight data lies within the third standard deviation is", len(weight_list_3_std) * 100.0 /len(weight_list))