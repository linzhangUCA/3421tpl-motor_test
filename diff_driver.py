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
  dd = DiffDriver(left_ids=(), right_ids=(), stby_id=)  # Fill in correct ids

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
