from flask_restful import  Api
from app import app
from app.resources.push import JiGuangPush
from app.resources.dingding import DingDingPunch,DingDingPunchList

api = Api(app)

api.add_resource(JiGuangPush, '/push')

api.add_resource(DingDingPunch,'/dingding/<string:_id>')
api.add_resource(DingDingPunchList,'/dingdings')