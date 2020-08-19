from flask import Flask
from numpyPseudoRNG import getRand
app = Flask(__name__)

@app.route("/numbers",)
def numbers():
  nums = getRand()
  print(nums)
  return str(nums)

numbers()
@app.route("/",)
def index():
  return "welcome to the pseudoRNG python server"


if __name__ == "__main__":
  app.run(host="ec2-54-183-155-131.us-west-1.compute.amazonaws.com", port=int("5000"))