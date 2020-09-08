from flask import Flask
import numpy as np
app = Flask(__name__)

@app.route("/numbers",)
def getByte():
    txt_data = open("data/pseudo_rng_data.txt","r")
    lines_count = 0
    for line in txt_data:
      line = line.strip("\n")
      lines_count += 1
    txt_data.close()
    txt_data = open("data/pseudo_rng_data.txt","r")
    rand_line = np.random.randint(1, lines_count)
    print("Randomly selected line: ",rand_line)
    current_byte = txt_data.readlines()[rand_line]
    print("Randomly selected byte: ",current_byte)
    txt_data.close()
    return str(current_byte)

getByte()
@app.route("/",)
def index():
  return "welcome to the pseudoRNG python server"

if __name__ == "__main__":
  app.run(host="ec2-54-193-121-13.us-west-1.compute.amazonaws.com", port=int("5000"))