for i in range(0, 100, 10):
    print(i)

    """"Here's what each part of the for loop using range() means:

start: The starting value of the sequence (inclusive). If not specified, it defaults to 0.
stop: The ending value of the sequence (exclusive). The for loop will iterate up to, but not including, this value.
step: The step or increment value for each iteration. If not specified, it defaults to 1.
In each iteration of the for loop, the loop variable (i in this case) takes on the next value from the sequence generated by range(). The loop body contains the code to be executed in each iteration.

Here's an example that demonstrates the usage of for loop with range():

python
Copy code
for i in range(1, 6, 2):
    print(i)
Output:

Copy code
1
3
5
In this example, the for loop iterates over the sequence generated by range(1, 6, 2). It starts at 1, increments by 2, and stops before reaching 6. In each iteration, the value of i is printed.




"""