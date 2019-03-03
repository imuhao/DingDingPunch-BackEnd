from app import app, jpushutils
from flask import request, jsonify
from flask_restful import Resource, Api, reqparse, abort
api = Api(app)


def abort_action_is_valid(action):
    if(action < 1 or action > 3):
        abort(404, message="action value range(1,3)")


parser = reqparse.RequestParser()
parser.add_argument('action', type=int, required=True)

class JiGuangPush(Resource):
    def post(self):
        args = parser.parse_args()
        abort_action_is_valid(args['action'])
        action = args['action']
        result = jpushutils.alias("Smile",action)
        if(result and result.status_code == 200):
            return {"error_code": 0, "error_msg": "推送成功!","action":action}
        else:
            return {"error_code": 404, "error_msg": "推送失败!"}

api.add_resource(JiGuangPush, '/push')
