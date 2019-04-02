from flask_restplus import Api, Resource, fields
from flask import Flask, request, jsonify
import math
import argparse

app = Flask(__name__)
api = Api(app, version='1.0', title='Make School Api', description='Automated Make Schooling')
ns = api.namespace('make_school_api', description='Methods')
single_parser = api.parser()
single_parser.add_argument('r', type=int, required=True, help="Radius")
single_parser.add_argument('h', type=int, required=True, help='Height')

# parser = argparse.ArgumentParser(description='This is a great description of what this does.')
# parser.add_argument('')

def cylinder_volume(radius, height):
  volume = (math.pi) * (radius ** 2) * height
  return volume

@ns.route('/volume')
class Volume(Resource):
  @api.doc(parser=single_parser, description='Enter two integers')
  def get(self):
    '''
    Uploads a new transaction to Rex(This is great!)
    '''
    args = single_parser.parse_args()
    radius = args.r
    height = args.h
    # r = request.args.get('r', type=int)
    # h = request.args.get('h', type=int)
    r = cylinder_volume(radius, height)
    # print(r)
    return jsonify({'Volume':r})

if __name__ == "__main__":
  app.run()