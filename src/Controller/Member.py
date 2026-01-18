from src.Model.Member import MemberModel
from src.app import app
from flask import request

@app.get("/member/add")
def memberAdd():
    userid = request.args.get("userid")
    if not userid and userid.count < 17 and userid.count > 18:
        return {"message": "Invalid Userid", "status": 400}
    else:
        member = MemberModel(userid=userid, perm=False)
        member.addUser()
        