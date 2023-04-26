import requests
import base64
import json
import tkinter
from tkinter import messagebox
import yaml


with open("config.yml", "r", encoding="utf-8") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
    uid = config["username"]
    psw = config["password"]
    domain = config["domain"]


def login(uid, psw, domain):
    UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " \
         "(KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"

    request_url = "http://10.102.250.13/index.php/index/login"

    request_headers = {
        "User-Agent": UA,
        "Referer": "http://10.102.250.13/",
        "Host": "10.102.250.13",
        "Origin": "http://10.102.250.13"
    }

    request_data = {
        "username": uid,
        "domain": domain,
        "password": base64.b64encode(psw.encode("utf-8")),
        "enablemacauth": "0"
    }

    top = tkinter.Tk()

    response = requests.post(request_url, headers=request_headers, data=request_data)
    response_json = json.loads(response.text)
    if response_json["status"] == 1:
        print("Login successfully.")
        messagebox.showinfo("提示", "网络登录成功！")
    elif response_json["status"] == 0:
        print("Login Already.")
        messagebox.showwarning("提示", "网络已登录！")
    else:
        print("Login failed.")
        print(response_json["info"])
        print(response_json)
        messagebox.showerror("提示", "网络登录失败！")
    top.destroy()
    return response_json


j = login(uid, psw, domain)

