import random 
import statistics
import plotly.figure_factory as ff
dice_result = []

for i in range(0, 1000):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_result.append(dice1 + dice2)

mean = sum(dice_result) / len(dice_result)
print("The mean is ", mean)

median = statistics.median(dice_result)
print("The median is ", median)

mode = statistics.mode(dice_result)
print("The mode is ", mode)

stdev = statistics.stdev(dice_result)
print("The standard deviation is ", stdev)

first_std_start, first_std_end = mean - stdev, mean + stdev
list_of_data_within_1_std = [result for result in dice_result if result > first_std_start and result < first_std_end]
print("Percentage of data lies within one standard deviation is ", len(list_of_data_within_1_std) * 100.0 / len(dice_result))

second_std_start, second_std_end = mean - (2 * stdev), mean + (2*stdev)
list_of_data_within_2_std = [result for result in dice_result if result > second_std_start and result < second_std_end]
print("Percentage of data lies within 2 standard deviation is ", len(list_of_data_within_2_std) * 100.0 / len(dice_result))

third_std_start, third_std_end = mean - (3*stdev), mean + (3*stdev)
list_of_data_within_3_std = [result for result in dice_result if result > third_std_start and result < third_std_end]
print("Percentage of data lies within 3 standard deviation is ", len(list_of_data_within_3_std) * 100.0 / len(dice_result))

# fig = ff.create_distplot([dice_result], ["result"], show_hist=False)
# fig.show()