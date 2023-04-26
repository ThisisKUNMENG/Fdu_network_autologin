# Fdu_network_autologin

* 用于解决电脑启动时iFudan.stu的自动登录

## 使用方法
1. 下载autologin-new.py以及config.yml
2. 填写config文件中用户名(username)、密码(password)、认证域(domain)
   * 其中认证域：校园网填fudan；中国移动填CMCC；中国联通填unicom-pppoe
3. 将py文件变成开机自启就行啦（运行py文件即可登录校园网）
   * 注意：需要安装requests库

---
* 以下为过时的autologin.py使用方法
1. 下载autologin.py
2. 填写py文件中用户名、密码、认证域
3. 将py文件变成开机自启就行啦
   * 注意：代码将使用chromedriver调用chrome,请提前安装chromedriver!
