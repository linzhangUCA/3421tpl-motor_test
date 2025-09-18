# Spin Motors

## Objectives
- Configure the motor driver board (TB6612FNG).
- Practice class inheritance, modification and instantiation.


## Requirements

### 1. Physical Configuration
You will configure the motor driver board slightly different from the example.

#### 1.1. Wiring Pico and Motor Driver Board
- Control left motor using `A` channel of the motor driver board.
- Control right motor using `B` channel.
- Use `GPIO7` for left motor's `PWM` input.
- Use `GPIO9` for left motor's `IN1` input.
- Use `GPIO8` for left motor's `IN2` input.
- Use `GPIO15` for right motor's `PWM` input.
- Use `GPIO13` for right motor's `IN1` input.
- Use `GPIO14` for right motor's `IN2` input.

#### (10%) 1.2 Circuit Picture
- Please take a picture of your circuit and display it below 👇

> [!IMPORTANT]
> Please make sure your picture **clearly** illustrates the wiring as required above.

> [!NOTE]
> Only the signal wiring section is required.
> No need for illustrating the motor and battery connections. 

![circuit_pic](circuit_pic.jpg)

### 2. Coding Exercises

#### 2.1. Build `DiffDriver` Class from Inheritance
Work in [diff_driver.py](diff_driver.py).
Develop a `DiffDriver` class by inheriting `DualMotorDriver` class.

1. Import correct module and inherit the `DualMotorDriver` class.
2. Introduce the following four methods/functions to the `DiffDriver` class and achieve the requested behavior.
   - `left_forward()`: drives mobile base forward and leaning left.
   - `right_forward()`: drives mobile base forward and leaning right. 
   - `left_backward()`: drives mobile backward and leaning left.  
   - `right_backward()`: drives mobile base backward and leaning right.
> [!WARNING]
> Nothing is allowed to be explicitly imported from `machine`.

> [!TIP]
> - Upload [motor_driver.py](https://github.com/linzhangUCA/3421example-motor_control/blob/main/motor_driver.py) and [dual_motor_driver.py](https://github.com/linzhangUCA/3421example-motor_control/blob/main/dual_motor_driver.py) to your Pico board.
> - Learn more about class inheritance from an interactive [tutorial](https://www.w3schools.com/python/python_inheritance.asp)
> - Test code has been included in [diff_driver.py](diff_driver.py). 

#### 2.2. Use `DiffDriver` Class
Please complete code in [test_diff_drive.py](test_diff_drive.py) to instantiate the `DiffDriver` class and use it to spin the motors.
1. Import correct module and instantiate an object using `DiffDriver` class. 


   
## AI Usage Policy
Please acknowledge AI's contribution following policies in the [syllabus](https://linzhanguca.github.io/_docs/robotics1-2025/syllabus.pdf).
