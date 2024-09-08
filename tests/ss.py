# 

def loop(steps):
    k=1
    # If steps are 10 or fewer, print each step
    if steps <= 10:
        step_interval = 1
    else:
        # Divide into 10 equal intervals
        step_interval = steps // 10
    
    printed_steps = 0  # Count the number of printed steps

    for step in range(0, steps + 1, step_interval):
        if printed_steps < 10:
            # print(f'Step: {step}')
            printed_steps += 1
            k+=1

    # If we didn't hit exactly 10 steps (due to rounding), print the final step
    if printed_steps < 10 and step != steps:
        # print(f'Step: {steps}')
        k+=1  # Ensure the last step is always printed

    print(f'steps:{steps}, k:{k}')

for iter in range(11,1000):
    loop(iter)
