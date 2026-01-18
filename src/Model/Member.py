from src.Model.Base import database
from pymongo import collection

class MemberModel(collection):
    def __init__(self, userid: str, perm: bool):
        self.userid = userid
        self.perm = perm
        self.member = database.member
    def findByUserId(self):
        results = self.member.find_one({"userid": self.userid})
        return results
    def findByPerm(self):
        results = self.member.find_one({"perm": self.perm})
        return results
        
    def addUser(self):
        docs = {
            "userid": self.userid,
            "perm": self.perm
        }
        self.member.insert_one(docs)
    def removeUser(self):
        results = self.member.delete_one({"userid": self.userid})
        return results.acknowledged
    