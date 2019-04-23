from flask_restful import Resource, Api, reqparse, abort
from werkzeug.datastructures import FileStorage
from app import photos,db
from app.utils import timeutils
import json
from bson.objectid import ObjectId

parser = reqparse.RequestParser()
parser.add_argument('photo', type=FileStorage, required=False,location='files')
parser.add_argument('action',type=int,required=False)
parser.add_argument('status',type=int,required=False)

class DingDingPunchList(Resource):
    def post(self):
        args = parser.parse_args()
        if "photo" in args.keys():
            filename = photos.save(args['photo'])
            # file_url = photos.url(filename)
        else:
            filename = ""
        punch = {
            "photo":filename,
            "action":args['action'],
            "status":args['status'],
            "time":timeutils.current_time()
        }
        db.punchs.insert(punch)
        return {"message":"上传成功!"}

    def get(self):
        args = parser.parse_args()
        argsNotNone = {k: v for k, v in args.items() if v is not None}

        punchs = db.punchs.find(argsNotNone)
        result = []
        for punch in punchs:
            punch["_id"] = str(punch["_id"])
            if(punch["photo"] ):
                punch["photo"] = photos.url(punch['photo'])
            result.append(punch)
        return {"result":result}


class DingDingPunch(Resource):
    def delete(self,_id):
        res= db.punchs.remove({"_id":ObjectId(_id)})
        return {"message":res}

