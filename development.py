from flask import Flask
from numpyPseudoRNG import getRand
app = Flask(__name__)



@app.route("/numbers/",)
def numbers():
  nums = getRand()
  numStr = str(nums)
  print(nums)
  print(type(numStr))
  return numStr

numbers()
@app.route("/",)
def index():
  return "welcome to the pseudoRNG python server"


if __name__ == "__main__":
  app.run(host="localhost", port=int("5001"))
