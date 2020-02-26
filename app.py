from flask import Flask
from robot import robot
from werobot.contrib.flask import make_view

app = Flask(__name__)
app.add_url_rule(rule='/WechatBot/',        # WeRoBot挂载地址
                 endpoint='werobot',             # Flask的endpoint
                 view_func=make_view(robot),
                 methods=['GET', 'POST'])


if __name__ == '__main__':
    app.run()
