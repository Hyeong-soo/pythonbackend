from typing import Union
import pyrebase
import json
import pams_crawling
from fastapi import FastAPI
from pydantic import BaseModel
from selenium import webdriver

app = FastAPI()
with open("auth.json") as f:
    config = json.load(f)

@app.get("/pams/{userid}&&{userpw}")
def read_user_me(userid:str, userpw:str):
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

    #userid = "hth021002"
    #userpw = "h1t0h2#vhsrrjHAN2"

    basicInfo_list, resume_list, schoolAct_list, clubAct_list, volunteer_list, extraAct_list = pams_crawling.get_user_info(userid, userpw)


    name = basicInfo_list[1]

    basic_dict = {"state":basicInfo_list[0], "schoolId":basicInfo_list[2], "major":basicInfo_list[3], "grade":basicInfo_list[4]}

    #기본정보 저장
    db.child("users").child(name).child("기본정보").set(basic_dict)

    #이력서 저장
    if resume_list[0] == "조회된 결과가 없습니다.":
        return {"isCorrect": "password is not correct!"}
    else :
        for info in resume_list:
            db.child("users").child(name).child("이력서").push(info)
        return {"isCorrect": "the current user"}





# signin = {"password":"qwerqwer", "username":"TaeHyeok"}

# db.child("users").child("hth021002").set(signin)

# for info in basicInfo_list:


#     cursor.execute(
#         f"INSERT INTO melon VALUES({i},\"{item[0]}\",\"{item[1]}\")")
#     i += 1
