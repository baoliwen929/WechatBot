from werobot import WeRoBot
# import user_sql
# from user_sql import cursor, users_db

robot = WeRoBot(
    token='baoliwen',  
    encoding_aes_key='jMxaDduuAykGrTskpemUgtX2FMUIdMNx7ljwVPfNRJs', 
    app_id='wx692d6f09312960ff'
)

# wechatbot_user = user_sql.Wechat_SQL(users_db, cursor)

@robot.text
def register(message):
    WECHATID = message.source
    user_group = robot.client.get_group_by_id(WECHATID)
    if user_group == "Foxboro":
        return "Foxboro Employee"
    else:
        return "Sorry, We are in testing and will serve you later. Thanks"


