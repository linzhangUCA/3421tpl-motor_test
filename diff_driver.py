"""
Import correct modules and build a DiffDriver class upon them.
Refer to: https://github.com/linzhangUCA/3421example-motor_control
"""
### START CODING HERE

### END CODING HERE

# TEST (change below code under your own risk)
if __name__=="__main__":
  # IMPORT
  from time import sleep
  
  # SETUP/INSTANTIATE
  dd = DiffDriver(right_ids=(9, 11, 10), left_ids=(15, 13, 14), stby_id=12)  # Feel free to change this

  # LOOP
  dd.left_forward()
  print("LF")
  sleep(4)
  dd.right_forward()
  print("RF")
  sleep(4)
  dd.left_backward()
  print("LB")
  sleep(4)
  dd.right_backward()
  print("RB")
  sleep(4)

  # Terminate
  dd.stop()
  print("motors stopped.")
  sleep(0.1)  # full stop
  dd.disable()  # disable motor driver
  print("motor driver disabled.")
