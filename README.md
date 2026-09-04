Python Loop Simulations
Project Overview
The two Python programs I created are the Smart Water Tank project and the Quantitative Growth project.

The important concepts these two programs have in common are:

using while loops
creating reusable functions
using conditions
testing edge cases
tracking and updating program state
These two programs belong in one repository because they both model real-world situations and use while loops to continue changing a value until a condition is met.

Smart Water Tank
The Smart Water Tank models a real-life water tank with a maximum capacity and a constant pump rate.

The main state variable in the Water Tank project is current_level. Its value changes when pump_rate is added to it.

The condition that controls the while loop is whether current_level is less than target_level.

I used:

min(current_level + pump_rate, 100)
inside pump_water() because if current_level and pump_rate add up to something greater than 100, min() chooses 100 instead. The returned value is then stored in the variable current_level.

pump_water() is reusable because it can be called with different arguments.

One important problem I discovered was the difference between limiting only the displayed value and limiting the actual stored water level.

If I only limit the displayed value, the actual stored water level could still exceed 100. A real water tank cannot hold more than its maximum capacity. If I limit the actual stored water level instead, current_level never exceeds 100, and the displayed level also stays at or below 100.

Another important edge case is pump_rate = 0.

If pump_rate is zero, current_level is below the target, and the program does not validate the pump rate, current_level does not change during each iteration. Therefore:

current_level < target_level
never becomes False, and the loop continues indefinitely.

My validation checks that pump_rate is greater than zero before the program starts the fill simulation.

Quantitative Growth
The function periods_to_target() calculates how many periods are required to meet or exceed a target amount.

The main state variable is current_amount because starting_amount is the initial value while current_amount changes each period.

The condition controlling the loop is:

current_amount < target_amount
The state is updated every period using:

current_amount *= growth_rate + 1
The function returns the number of periods.

The parameters have different purposes:

starting_amount gives the function its initial state.
growth_rate determines the rate at which the current amount grows.
target_amount gives the function the target it is trying to reach.
Compounding
The growth in this program is multiplicative rather than additive because the program models compounding.

In my own words, compounding means that each new amount is calculated from the entire accumulated amount from the previous period.

For example, suppose the starting amount is $1,000 and the growth rate is 5%.

The growth factor is:

1 + 0.05 = 1.05
So the amounts grow like this:

1000 × 1.05 = 1050
1050 × 1.05 = 1102.50
The growth rate stays constant, while current_amount changes. Growth applies to the entire accumulated amount from the previous period.

For the case:

(1000, 0.05, 1500)
the program requires nine periods to meet or exceed the target.

For the case:

(1600, 0.05, 1500)
the program requires zero periods because the target has already been exceeded. Since:

1600 < 1500
is False, the while loop does not execute.

Zero-Growth Edge Case
A growth rate of zero is an important edge case.

If starting_amount is less than target_amount and the growth rate is zero, then without validation, current_amount never moves toward the target.

For example:

starting_amount = 1000
target_amount = 1500
growth_rate = 0
The update effectively becomes:

1000 × 1 = 1000
so current_amount < target_amount remains True and the loop would continue indefinitely.

The program does not necessarily produce an error. Instead, without validation, the loop keeps running because its state does not move toward the target.

My validation handles this before the while loop begins:

growth_rate <= 0 and starting_amount < target_amount
If the starting amount is already greater than or equal to the target amount, the loop executes zero times.

Testing and Edge Cases
Testing only a normal case is not enough because there may be other inputs that produce incorrect behavior.

For example, in the Quantitative Growth program, if I had tested only the normal case, I could have missed the zero-growth edge case. When the starting amount is below the target, a growth rate of zero can cause an infinite loop without validation.

Testing normal cases and edge cases can reveal logical errors and flaws in a program. Fixing the errors we find does not mean that the code is perfect, but testing many different cases can increase our confidence that the program behaves correctly.

Two important edge cases I tested were:

Smart Water Tank: pump_rate = 0
Quantitative Growth: starting_amount >= target_amount
In the Water Tank program, a zero pump rate while the current level is below the target would prevent the state from changing, causing the loop to continue indefinitely without validation.

In the Quantitative Growth program, I tested a starting amount of 1600 with a target of 1500:

1600 < 1500 → False
If a while condition is False before the first iteration, the loop does not execute at all. Therefore, this case requires zero periods and is not an infinite loop.

I learned that I can examine the state, condition, and update to predict whether a loop will eventually terminate. I can look at the starting state and the condition, then examine how the update changes the state and whether it moves the program toward making the condition False.

What I Learned
One of my biggest misunderstandings while developing these programs involved reusable functions.

I learned that parameters allow a function to work with different inputs and that return values allow a function to send a result back to the code that called it. Reusable functions are especially useful when testing different cases.

Debugging taught me not only to understand correct code, but also to understand and explain what went wrong with incorrect code, including syntax errors and logical errors. This helped me become better at finding problems in my own code.

I also learned that exact boundaries are very important.

For example, if the requirement is for the water level to reach or exceed the target, the loop can continue while:

current_level < target_level
When current_level becomes equal to the target, the condition becomes False and the requirement has been reached.

Using the wrong boundary can cause an extra iteration or incorrect behavior.

Another important lesson was the difference between what a program displays and what it actually stores.

In an earlier version of the Water Tank program, the program could display a maximum level of 100 while internally storing a value such as 107. That was a problem because the tank should not actually hold more than 100.

For example, if the current level is 92 and the pump rate is 15, the original pump_rate is still 15. However, the tank can accept only 8 additional percentage points before reaching its capacity. The new stored current_level should therefore be 100.

This taught me that fixing only the displayed output does not necessarily fix the program's actual state.

Reflection
The Smart Water Tank project was harder for me than the Quantitative Growth project.

One reason was that there were several edge cases to consider, and these were where I got stuck the most. Working with reusable functions was also challenging because I had to think carefully about the purpose of each function, its parameters, and its returned values.

The Water Tank scenario was also harder to model because I needed to make sure that the stored water level, not just the displayed value, had a maximum of 100.

The problem I am most proud of figuring out was the storage limit of the Water Tank. Solving this problem made the simulation behave more realistically and fixed an important error in the program.


One thing I want to improve is my accuracy. It took me several tries to get these programs right. I want to become better at predicting problems, testing edge cases, and checking my logic so that I can solve future problems more accurately.
