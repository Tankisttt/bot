
# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request, json
import vk
import random
import mysql.connector
#from settings import *
#import messageHandler
token = 'c417ab21a011239494ec567878a6f5cd03aca821668ab2151a06a9bdf93a3e9a03b1fea992cce6967432b'
confirmation_token = '85ac9ec9'
session = vk.Session()
api = vk.API(session, v=5.92)
app = Flask(__name__)
@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        id=data['object']['from_id']
        message=data['object']['text']
        if 'payload' in data['object'].keys():
            payload=data['object']['payload']
            strpayload=json.loads(payload)
            #if strpayload['test']=='red':
                #session = vk.Session()
                #api = vk.API(session, v=5.92)
                #api.messages.send(user_id=str(id),random_id=random.randint(1,90000000000000),access_token=token,keyboard=json.dumps({'one_time':True,'buttons':[]}))
                #return 'ok'
        else: payload=None
        if 'peer_id' in data['object'].keys():
            peer_id=data['object']['peer_id']
        else: peer_id=None
        #kwargs={"ensure_ascii":False,"separators":(',',':')}
        #kwargs['ensure_ascii'] = False
        #kwargs['separators'] = (',', ':')
        ##keyboard=json.dumps({'one_time': False,'buttons': [[{'action': { 'type': 'text','payload': json.dumps({'test':'red'}, kwargs),'label': 'Lol'},'color': 'positive'},{'action':{'type': 'text','payload': json.dumps({'test':'some_payload'}, kwargs),'label': 'Green'},'color': 'positive'}],[{'action': {'type': 'text','payload': json.dumps({'test':'some_payload'}, kwargs),'label': 'White'},'color': 'default'},{'action': {'type': 'text','payload': json.dumps({'test':'some_payload'}, kwargs),'label': 'Blue'},'color': 'primary'}]]},kwargs)
        ##emptykeyboard=json.dumps({'one_time':True,'buttons':[[]]})
        rand=data['object']['random_id']
        ##api.messages.send(user_id=str(id),random_id=random.randint(1,90000000000000),access_token=token,message='ZHMI KRASNYY',keyboard=emptykeyboard)
        ##return 'ok'
        keyboard=json.dumps({'one_time': False,'buttons': [[{'action': { 'type': 'text','payload': json.dumps({'test':'red'}),'label': 'Red'},'color': 'negative'},{'action':{'type': 'text','payload': json.dumps({'test':'green'}),'label': 'Green'},'color': 'positive'}],[{'action': {'type': 'text','payload': json.dumps({'test':'white'}),'label': 'White'},'color': 'default'},{'action': {'type': 'text','payload': json.dumps({'test':'blue'}),'label': 'Blue'},'color': 'primary'}]]})
        #keyboard = {
        #    'one_time': False,
        #    'buttons': [
        #       [
        #            {
        #                'color': 'default',
        #             '  action': {
        #                     'type': 'text',
        #                     'payload': json.dumps({'test': 'some_payload'}, kwargs),
        #                     'label': 'Test-1'
        #                }
        #            }
        #        ],
        #        []
        #    ]
        #}


        api.messages.send(user_id=str(id),random_id=int(id)+random.randint(1,90000000000000),access_token=token,message=str("Anton1"))
        api.messages.send(user_id=str(id),random_id=int(id)+random.randint(1,90000000000000),access_token=token,message=str("Anton2"))
        newmes=gettheme()
        ##api.messages.send(user_id=str(id),random_id=int(id)+random.randint(1,90000000000000),access_token=token,message=str(newmessage),keyboard=keyboard)
        api.messages.send(user_id=str(id),random_id=int(id)+random.randint(1,90000000000000),access_token=token,message=str(newmes))
        ##api.messages.send(user_id=str(id),random_id=random.randint(1,90000000000000),access_token=token, message='Привет, я новый бот!')




        #paylo=r'{\"command\":\"start\"}'
        #button=json.dumps({'action':{'type':"messag",'payload':str(paylo),'label':"Red"},'color':"positive"},separators=(',', ':'))
        #keyboard=json.dumps({'one_time':True,'buttons':[[str(button),str(button)],[str(button)]]}, separators=(',', ':'))
        #user_id=str(id),random_id=data['object']['random_id'],access_token=token, group_id=str(data['group_id']
        return 'ok'
def gettheme():
    api.messages.send(user_id=str(id),random_id=int(id)+random.randint(1,90000000000000),access_token=token,message=str("10"))
    mydb=mysql.connector.connect(user='pokemongo12345',password='Caranell123',host='pokemongo12345.mysql.pythonanywhere-services.com',database='pokemongo12345$VkBot')
    api.messages.send(user_id=str(id),random_id=int(id)+random.randint(1,90000000000000),access_token=token,message=str("1"))
    curs = mydb.cursor()
    api.messages.send(user_id=str(id),random_id=int(id)+random.randint(1,90000000000000),access_token=token,message=str("2"))
    curs.execute("select * from name")
    api.messages.send(user_id=str(id),random_id=int(id)+random.randint(1,90000000000000),access_token=token,message=str("3"))
    result = curs.fetchall()
    api.messages.send(user_id=str(id),random_id=int(id)+random.randint(1,90000000000000),access_token=token,message=str("4"))
    #varchar требуется привести к string с соответстввующей кодировкой
    lines=""
    for string in result:
        lines+=((str(string[0]) + " " + str(string[1], "utf-8"))+'\n')
    api.messages.send(user_id=str(id),random_id=int(id)+random.randint(1,90000000000000),access_token=token,message=str("5"))
    curs.close()
    api.messages.send(user_id=str(id),random_id=int(id)+random.randint(1,90000000000000),access_token=token,message=str("6n"))
    return lines