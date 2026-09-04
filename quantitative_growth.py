# The state variable is starting_amount.
# The starting state is 1000.
# The stopping condition is at least 1500.
# The update rule is to increase by 5%.
# This is multiplicative growth because if you are increasing a value by 5%, you are technically multiplying
# the value by 1.05. which is mulitplicative growth.
# I do expect 10 periods to be enough. Even though growing by 5% might not seem like a lot, this is a
# type of compounding, meaning that there is exponential growth. Since you only have to grow 500 dollars
# over 10 periods, it can be enough.

def periods_to_target(starting_amount, growth_rate, target_amount):
    if growth_rate <= 0 and starting_amount < target_amount:
        print("Invalid growth rate. Enter a valid growth rate.")
        return
    period_number = 0
    current_amount = starting_amount
    if current_amount >= target_amount:
        print(f"Period {period_number}: {current_amount}")
    while current_amount < target_amount:
        current_amount *= growth_rate + 1
        period_number += 1
        print(f"Period {period_number}: {current_amount}")
    return period_number
periods_to_target(1000, 0.05, 1500)
# Required Test A: 1000, 0.05, 1500
# There will be 9 periods.
# Period 1: 1050.0
# Period 2: 1102.5
# Period 3: 1157.625
# Period 4: 1215.5062500000001
# Period 5: 1276.2815625000003
# Period 6: 1340.0956406250004
# Period 7: 1407.1004226562504
# Period 8: 1477.455443789063
# Period 9: 1551.3282159785163
# The result makes mathematical sense because as the periods increase by 5%, there will not be whole numbers
# after you get through the second period and beyond. Plus, the periods count from 1 to 9 and end at 1551, which
# is higher than the goal of 1500.

# Required Test B: 1000, 0, 1500
# If the program entered a while loop with growth_rate = 0 and the starting amount were below the target,
# the program would show an error that reads Invalid growth rate. If that condition was removed,
# there would be no protection for the code, causing an infinite loop. A 0% growth rate would be dangerous
# because a while loop runs until it turns false, meaning that if the current amount never reaches the target amount,
# the code will run forever and crash.

# Required Test C
# The starting amount is $1600.
# The target amount is $1500.
# The starting amount already exceeded the target amount.
# Zero periods of growth are necessary.
# The loop condition target_amount > starting_amount would be false.
# If this is the condition, the while loop will not execute even once.
# If the loop never starts, the loop cannot be infinite because the current amount already exceeded the target amount.
# If the target has been reached before Period 1, the function should return zero periods and print the current amount.

# 1000, 0.05, 1500; The result is correct because there are 9 periods, which is correct via compounding. The program
# also stops at a value bigger than the target value, which is correct.
# 1000, 0.00, 1500; The result is correct because the code rejects zero as a growth rate. If there was no validation,
# the code would never make the current amount ever reach the target amount, making the code run forever.
# 1600, 0.05, 1500; The result is correct because the current value already exceeded the target value, which means that
# there should be no errors and zero periods required.
# 1500, 0.05, 1500; This case is correct because the target value equals the current value, which means that there
# should be zero periods required.
# The 1600 -> 1500 case is not an infinite loop because the current amount is already bigger than the target amount.
# In this case, zero periods are required, meaning that this case is not an infinite loop.
