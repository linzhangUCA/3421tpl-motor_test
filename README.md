# Spin Motors

## Objectives
- Configure the motor driver board (TB6612FNG).
- Practice class inheritance, modification and instantiation.


## Requirements

### 1. (35%) Physical Configuration
You will configure the motor driver board slightly different from the example.

#### 1.1. Wiring Pico and Motor Driver Board
- Control left motor using `A` channel of the motor driver board.
- Control right motor using `B` channel.
- (5%) Use `GPIO7` for left motor's `PWM` input.
- (5%) Use `GPIO9` for left motor's `IN1` input.
- (5%) Use `GPIO8` for left motor's `IN2` input.
- (5%) Use `GPIO15` for right motor's `PWM` input.
- (5%) Use `GPIO13` for right motor's `IN1` input.
- (5%) Use `GPIO14` for right motor's `IN2` input.
- (5%) Use `GPIO12` for motor driver's `STBY` input.

#### 1.2. Circuit Picture
- Please take a picture of your circuit and display it below 👇

![circuit_pic](circuit_pic.jpg)

> [!IMPORTANT]
> - Please make sure your picture **clearly** illustrates the wiring as required above.
> - You'll get your points after picture is correctly rendered.  
> - Only the signal wiring section is mandatory.
> illustrating motor and battery connections is optional. 

### 2. (65%) Coding Exercises

#### 2.1. (55%) Build `DiffDriver` Class from Inheritance
Work in [diff_driver.py](diff_driver.py).
Develop a `DiffDriver` class by inheriting `DualMotorDriver` class.
> [!WARNING]
> - Nothing is allowed to be explicitly imported from `machine`.
> IOW, do not use `Pin`, `PWM`, `Timer`, etc..
 
1. (5%) Import correct module and inherit the `DualMotorDriver` class.
2. (10%) Instantiate a `DualMotorDriver` object under the line `if __name__=="__main__":`. Please strictly follow the motor channel definitions in [Wiring Pico and Motor Driver Board](#11-wiring-pico-and-motor-driver-board) section.
3. Introduce the following four methods/functions to the `DiffDriver` class and achieve the requested behavior.
   - (10%) `forward_left()`: drives mobile base forward and leaning left.
   - (10%) `forward_right()`: drives mobile base forward and leaning right. 
   - (10%) `backward_left()`: drives mobile backward and leaning left.  
   - (10%) `backward_right()`: drives mobile base backward and leaning right.

> [!IMPORTANT]
> - No need for variable motor speed.
> - Please use 50% max speed for the faster motor and 25% max speed for the slower motor.

> [!TIP]
> - Upload [motor_driver.py](https://github.com/linzhangUCA/3421example-motor_control/blob/main/motor_driver.py) and [dual_motor_driver.py](https://github.com/linzhangUCA/3421example-motor_control/blob/main/dual_motor_driver.py) to your Pico board.
> - Learn more about class inheritance from this interactive [tutorial](https://www.w3schools.com/python/python_inheritance.asp)
> - Test newly developed functions frequently using the test code under the line: `if __name__=="__main__":`. 

#### 2.2. (10%) Use `DiffDriver` Class
Please complete code in [test_diff_drive.py](test_diff_drive.py) to instantiate the `DiffDriver` class and use it to spin the motors.
1. (2%) Import correct module and instantiate an object using `DiffDriver` class.
2. (8%) Perform the following sequence of operations on mobile base. Each operation should last for **1 second**.
     1. (1%) `forward(0.5)`
     2. (1%) `forward_left()`.
     3. (1%) `spin_left(0.5)`.
     4. (1%) `backward_left()`.
     5. (1%) `backward(0.5)`.
     6. (1%) `backward_right()`
     7. (1%) `spin_right(0.5)`
     8. (1%) `forward_right()`


   
## AI Usage Policy
Please acknowledge AI's contribution following policies in the [syllabus](https://linzhanguca.github.io/_docs/robotics1-2025/syllabus.pdf).
