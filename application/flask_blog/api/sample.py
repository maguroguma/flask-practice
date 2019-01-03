from flask import jsonify, abort, make_response, Blueprint

from flask_blog import app

api = Blueprint('api', __name__)

@api.route('/get', methods=['GET'])
def get():
  result = { 'greeting': 'hello flask' }
  return make_response(jsonify(result))

@api.errorhandler(404)
def not_found(error):
  return make_response(jsonify({ 'error': 'Not found' }), 404)
