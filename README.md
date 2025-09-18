# Motors Spin-Up

## Objectives
- Implement modular software development using object-orient programming paradim.
- Practice class inheritance, modification and instantiation.
- Explore different configurations using the motor driver board (TB6612FNG).
- Roughly estimate motor speed. 

## Requirements

### 1. Physical Configuration
You will configure the motor driver board slightly different from the example.

#### 1.1. Wiring Pico and Motor Driver Board
- Control right motor using `A` channel of the motor driver board.
- Control left motor using `B` channel.
- Use `GPIO7` for left motor's `PWM` input.
- Use `GPIO9` for left motor's `IN1` input.
- Use `GPIO8` for left motor's `IN2` input.
- Use `GPIO15` for right motor's `PWM` input.
- Use `GPIO13` for right motor's `IN1` input.
- Use `GPIO14` for right motor's `IN2` input.

#### (10%) 1.2 Circuit Picture
- Please take a picture of your circuit and display it below 👇
- Please make sure your picture clearly illustrates the correct wiring as required above.

> [!NOTE]
> Only the signal wiring section is required.
> No need for illustrating the motor and battery connections. 

![circuit_pic](circuit_pic.jpg)

### 2. Coding Exercises
Upload the [example scripts](https://github.com/linzhangUCA/3421example-motor_control) to your Pico.
Develop a `DiffDriver` class by inheriting `DualMotorDriver` class.

1. Import correct module and inherit the `DualMotorDriver` class
2. Introduce the following four methods/functions to the `DiffDriver` class and achieve the requested behavior.
   - `left_forward()`: drives mobile base forward and leaning left.
   - `right_forward()`: drives mobile base forward and leaning right. 
   - `left_backward()`: drives mobile backward and leaning left.  
   - `right_backward()`: drives mobile base backward and leaning right.
> [!IMPORTANT]
>  Use `50000` and `30000` as the `duty_u16()` value for the faster and the slower motor.

#### 1.1 Inherit 
Complete the Python scripts and answer the questions by editing the [README](/README.md) file. 
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
Make marks on both wheels at same spot before you start the testing [script](/estimate_speed.py). Run testing script and observe the motors behaviors carefully.
1. (10%) Complete the testing script: [estimate_speed.py](/estimate_speed.py). Spin both motors on same direction with 50% duty cycle PWM signals. Let the spinning last for 1 minute. Then stop.
> **Hint**: No loop is needed.
2. (30%) Observe the motor's behavior carefully and answer the questions below.
   1. (20%) Can you estimate the speed of each motor using "revolutions per minute (RPM)"? Please round the RPM to **one decimal place**. 
      > Your answer here.
   2. (10%) What would be the reasons if the speeds of the motors were different? 
      > Your answer here.
3. (10%) Upload images to show final location of the marks on each wheel. 
   
## AI Usage Policy
Please give credits to your AI assistance. Refer to the [syllabus](https://linzhanguca.github.io/_docs/robotics1-2024/syllabus.pdf) for the citation format.
