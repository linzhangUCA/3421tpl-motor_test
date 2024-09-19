# Motor Test
In this assignment, you'll test the motor driver with the Pico board. Complete the scripts to veriify motors are functional and wiring is correct.
  
## Requirements:
### (50%) [ramp_up_down.py](/ramp_up_down.py)
Slowly increase and decrease both motors' speed. Both motors should take actions at the same time.
1. (10%) Ramp up both motors' speed (from stall to max) in 4 seconds. Spin both motors **forward**.
2. (10%) Slow down both motors' speed (from max to stall) in 4 seconds. Spin both motors **forward**.
3. (10%) Ramp up both motors' speed (from stall to max) in 4 seconds. Spin both motors **backward**.
4. (10%) Slow down both motors' speed (from max to stall) in 4 seconds. Spin both motors **backward**.
5. (10%) Stop both motors.
> **Hint**:
> - you may want to refer to the `fade_in_fade_out.py` from your second assignment.
> - No loop is needed.

### (50%) Estimate Motor Speed
Make marks on both wheels at same spot before you start the testing [script](/spin_2min.py). Run testing script
1. (10%) Complete the script: [spin_2min.py](/spin_2min.py).
   - (10%) Spin both motors with 50% duty cycle PWM signals. Let the spinning last for 2 minutes. Then stop.
> **Hint**: No loop is needed.
2. (30%) Observe the motor's behavior carefully and answer the questions below.
   1. (20%) Can you estimate the speed of each motor in "revolutions per minute (RPM)"? Please use **one decimal place**. 
      > Your answer here.
   2. (10%) Whay would be the reasons if the speeds of the motors were different? 
      > Your answer here.
3. (10%) Upload evidence
Upload an image 
