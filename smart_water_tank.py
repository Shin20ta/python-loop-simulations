# Cycle Water Level
# Start 23
# 1     34
# 2     45
# 3     56
# 4     67
# 5     78
# 6     89
# Number of Cycles: 6
# Final Water Level: 89
# Stops at 85%: No


def is_valid_percentage(value):
    return value >= 0 and value <= 100
    
def pump_water(current_level, pump_rate):
    return min(current_level + pump_rate, 100)
    
def print_system_report(final_level, total_water, total_cycles, target):
    display_level = min(final_level, 100)
    print("--- FINAL SYSTEM REPORT ---")
    print(f"Final Water Percentage: {display_level}%")
    print(f"Total Water Volume Pumped: {total_water}%")
    print(f"Number of Cycles: {total_cycles}")
    
    if display_level == target:
        print(f"Stops at {target}%: Yes")
    else:
        print(f"Stops at {target}%: No")
def run_fill_simulation(starting_level, target_level, pump_rate):
    current_level = starting_level
    cycle = 0
    print("Cycle Water Level")
    print(f"Start {current_level}")
    while current_level < target_level:
        current_level = pump_water(current_level, pump_rate)
        cycle += 1
        print(f"Cycle {cycle}    Current Level: {current_level}")
            
    water_pumped = current_level - starting_level
    return current_level, water_pumped, cycle

    
def run_simulation(starting_level, target_level, pump_rate):
    valid_inputs = (
          is_valid_percentage(starting_level) and
          is_valid_percentage(target_level) and
          pump_rate > 0
    )
    if valid_inputs:
        final_lvl, total_wtr, total_cyc = run_fill_simulation(starting_level, target_level, pump_rate)
        print_system_report(final_lvl, total_wtr, total_cyc, target_level)
    else:
        print("Error: Invalid simulation parameters.")
        print("Percentages must be between 0 and 100.")
        print("Pump rate must be greater than 0.")

def main():
    run_simulation(23, 85, 11)

if __name__ == "__main__":
    main()


# Testing
# Test A
# Prediction: 6 cycles; 34, 45, 56, 67, 78, 89 for current level
# Actual result: 6 cycles, 34, 45, 56, 67, 78, 89 for current level
# Pass or Fail: Pass
# Why: The program passed because the current level fit the requirement, which was under 100%, and
# the current levels went up by 11 each time.
# Test B
# Prediction: 0 cycles
# Actual result: 0 cycles
# Pass or Fail: Pass
# Why: If the current level is higher than the target level at any given time, the program does not need to
# pump any water. Furthermore, since the target has already been reached, water does not need to be pumped because
# the requirement has already been met.
# Test C
# Prediction: 1 cycle; 8 percentage points added
# Actual result: 1 cycle; 8 percentage points added
# Pass or Fail: Pass
# Why: The result never exceeds 100 because in the function pump_water, the capacity limit is applied to the
# actual new water level. In this problem, eight percentage points was pumped into the tank instead
# of fifteen percentage points because the stored water level's absolute maximum capacity is 100.
# Test D
# Prediction: Error
# Actual result: Error: Pump rate must be greater than 0.
# Pass or Fail: Pass
# Why: The program rejects the pump rate and shows an error before entering the simulation loop because
# the program is designed to find no pump rates or negative pump rates before the loop starts.
# The code doesn't run forever because the code already checked if the pump rate is less than or equal to zero
# before the program does any calculations.
# If the pump_rate > 0 validation did not exist and the pump rate were 0 while the current level was below the target,
# the current_level would never move towards the target because no water is being pumped. This would create in infinite
# loop because the while condition will never turn false if the target level is never met.
# Test E: 90, 99, 2
# Prediction: 92, 94, 96, 98, 100
# Actual result: 92, 94, 96, 98, 100; 5 cycles
# Pass or Fail: Pass
# Why: The code should stop if the target has been exceeded or reached, and the code stops at 100.

# Edge Cases
# If the starting level is greater or equals to target, there would be no pumping cycles necessary because the target
# has already been met.
# If the pump rate is zero, the program shows an error.
# If the pump rate is negative, the program also shows an error.
# If the starting level is negative, there is an invalid simulation parameter.
# If the target is 120, the program shows an error.
# Real engineering software should validated data because you must make sure anything that is typed incorrectly
# does not crash a code.
# Testing only the "normal case" is dangerous because if you are working with something like a while loop,
# there is a possibility that the loop can run forever if the condition does not turn into false.
