import time
import numpy as np
import flask


def getRand():
  while True:
      numbers = np.random.randint(0,2,8)
      numStr = str(numbers)
      txt_data = open("data/pseudo_rng_data.txt","a")
      txt_data.write(numStr + "\n")
      txt_data.close()
      print(numbers)
      time.sleep(1)


getRand()