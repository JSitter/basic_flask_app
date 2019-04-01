from flask import Flask, request, jsonify
import math
import argparse

app = Flask(__name__)

# parser = argparse.ArgumentParser(description='This is a great description of what this does.')
# parser.add_argument('')

def cylinder_volume(radius, height):
  volume = (math.pi) * (radius ** 2) * height
  return volume

@app.route('/')
def main():
  r = request.args.get('r', type=int)
  h = request.args.get('h', type=int)
  r = cylinder_volume(r, h)
  print(r)
  return jsonify({'Volume':r})

if __name__ == "__main__":
  app.run()