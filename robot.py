from werobot import WeRoBot
 

robot = WeRoBot(
    token='baoliwen',  
    encoding_aes_key='jMxaDduuAykGrTskpemUgtX2FMUIdMNx7ljwVPfNRJs', 
    app_id='wx692d6f09312960ff'
)



@robot.handler
def hello(message):
    print (message.source)
    return message.source
