import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

API_TOKEN = '521206254:AAFApBL4zEpt-Gy347Vm5vIL0nrM54Iknnw'
# ngrok authtoken 4UPfcDVEPnZbVDYXC2Rpj_3W4xcafake48pkbF6mTbj
# ngrok.exe http 5000
WEBHOOK_URL = 'https://cc24a92b.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot ( token = '521206254:AAFApBL4zEpt-Gy347Vm5vIL0nrM54Iknnw' )

from fsm import TocMachine
from transitions import Machine
import random

app = Flask (__name__)
bot = telegram.Bot ( token = API_TOKEN )
machine = TocMachine (
    Statistics = ['成大統計'],
    Field = ['生物統計', '工業統計', '商業統計', '數理統計'],
    Introduction = ['「生物統計」是統計結合基因解碼資料去了解基因和疾病間的關係','「工業統計」課程如工業管理，會教導同學何謂魚骨圖與管制圖，再運用於工廠生產管理中','「商業統計」是運用統計數據做出適宜的金融商品投資決策','「數理統計」內容較為理論與艱深，是往後將統計學知識應用到各領域時最強大的後盾'],
    Teacher = ['馬瀰嘉','石瑜','楊明宗','潘浙楠','嵇允嬋','任眉眉','溫敏杰','陳瑞彬','詹世煌','趙昌泰','鄭順林','杜宜軒','張升懋','李國榮','蘇佩芳','林良靖','張欣民','李俊毅','李政德','李宜真','曾仲瑩','楊欣洲','吳致杰','吳鐵肩','呂金河','張紹洪','吳宗正','高正雄','許秀麗','夏啟峻','鄭碧娥','程毅豪'],

    Biological_Statistics_Teachers = ['馬瀰嘉','石瑜','詹世煌','鄭順林','杜宜軒','蘇佩芳','李政德','曾仲瑩','楊欣洲','吳致杰','程毅豪'],
    Industrial_Statistics_Teachers = ['潘浙楠','鄭順林','李俊毅','張欣民','李宜真'],
    Commercial_Statistics_Teachers = ['林良靖','吳宗正'],
    Mathematical_Statistics_Teachers = ['馬瀰嘉','楊明宗','嵇允嬋','任眉眉','溫敏杰','陳瑞彬','趙昌泰','張升懋','李國榮','林良靖','吳鐵肩','呂金河','張紹洪','高正雄','許秀麗','夏啟峻','鄭碧娥'],

    States = [
        '成大統計',
        '生物統計',
        '工業統計', 
        '商業統計', 
        '數理統計',
        '馬瀰嘉',
        '石瑜',
        '楊明宗',
        '潘浙楠',
        '嵇允嬋',
        '任眉眉',
        '溫敏杰',
        '陳瑞彬',
        '詹世煌',
        '趙昌泰',
        '鄭順林',
        '杜宜軒',
        '張升懋',
        '李國榮',
        '蘇佩芳',
        '林良靖',
        '張欣民',
        '李俊毅',
        '李政德',
        '李宜真',
        '曾仲瑩',
        '楊欣洲',
        '吳致杰',
        '吳鐵肩',
        '呂金河',
        '張紹洪',
        '吳宗正',
        '高正雄',
        '許秀麗',
        '夏啟峻',
        '鄭碧娥',
        '程毅豪'
    ],

    Transitions = [
        {
            'trigger' : 'Introduction',
            'source' : '成大統計',
            'dest' : '生物統計',
            'conditions' : 'Biological_Statistics'
        },
        {
            'trigger' : 'Introduction',
            'source' : '成大統計',
            'dest' : '工業統計',
            'conditions' : 'Industrial_Statistics'
        },
        {
            'trigger' : 'Introduction',
            'source' : '成大統計',
            'dest' : '商業統計',
            'conditions' : 'Commercial_Statistics'
        },
        {
            'trigger' : 'Introduction',
            'source' : '成大統計',
            'dest' : '數理統計',
            'conditions' : 'Mathematical_Statistics'
        },
    ],

    initial = '成大統計',
    auto_transitions = False,
    show_conditions = True,
)

for Biological_Statistics_Teacher in Biological_Statistics_Teachers:    
    random.shuffle ( Biological_Statistics_Teachers )
    Transitions = [
        {
            'trigger' : 'Teacher',
            'source' : '生物統計',
            'dest' : Biological_Statistics_Teachers[0],
            'conditions': 'Biological_Statistics_Teacher'
        },
    ]    

for Industrial_Statistics_Teacher in Industrial_Statistics_Teachers:    
    random.shuffle ( Industrial_Statistics_Teacher )
    Transitions = [
        {
            'trigger' : 'Teacher',
            'source' : '工業統計',
            'dest' : Industrial_Statistics_Teacher[0],
            'conditions': 'Industrial_Statistics_Teacher'
        },
    ]

for Commercial_Statistics_Teacher in Commercial_Statistics_Teachers:
    random.shuffle ( Commercial_Statistics_Teacher )
    Transitions = [
        {
            'trigger' : 'Teacher',
            'source' : '商業統計',
            'dest' : Commercial_Statistics_Teacher[0],
            'conditions': 'Commercial_Statistics_Teacher'
        },
    ]

for Mathematical_Statistics_Teacher in Mathematical_Statistics_Teachers:        
    random.shuffle ( Mathematical_Statistics_Teacher )
    Transitions = [
        {
            'trigger' : 'Teacher',
            'source' : '數理統計',
            'dest' : Mathematical_Statistics_Teacher[0],
            'conditions': 'Mathematical_Statistics_Teacher'
        },
    ]

machine.add_transition ( trigger = 'Information', source = '馬瀰嘉', dest = 'http://www.stat.ncku.edu.tw/UserFunc/ProfData/UserShowProfessor.asp?pid=8108165&keepThis=true&TB_iframe=true&height=500&width=800')
machine.add_transition ( trigger = 'Information', source = '石瑜', dest = 'http://www.stat.ncku.edu.tw/activities/20090405_DrShih/DrShih.html')
machine.add_transition ( trigger = 'Information', source = '楊明宗', dest = 'http://www.stat.ncku.edu.tw/UserFunc/ProfData/UserShowProfessor.asp?pid=5808025&keepThis=true&TB_iframe=true&height=500&width=800')
machine.add_transition ( trigger = 'Information', source = '潘浙楠', dest = 'http://www.stat.ncku.edu.tw/UserFunc/ProfData/UserShowProfessor.asp?pid=8108164&keepThis=true&TB_iframe=true&height=500&width=800')
machine.add_transition ( trigger = 'Information', source = '嵇允嬋', dest = 'http://www.stat.ncku.edu.tw/UserFunc/ProfData/UserShowProfessor.asp?pid=7802015&keepThis=true&TB_iframe=true&height=500&width=800')
machine.add_transition ( trigger = 'Information', source = '任眉眉', dest = 'http://www.stat.ncku.edu.tw/UserFunc/ProfData/UserShowProfessor.asp?pid=8008095&keepThis=true&TB_iframe=true&height=500&width=800')
machine.add_transition ( trigger = 'Information', source = '溫敏杰', dest = 'http://www.stat.ncku.edu.tw/UserFunc/ProfData/UserShowProfessor.asp?pid=8008094&keepThis=true&TB_iframe=true&height=500&width=800')
machine.add_transition ( trigger = 'Information', source = '陳瑞彬', dest = 'http://www.stat.ncku.edu.tw/UserFunc/ProfData/UserShowProfessor.asp?pid=10002011&keepThis=true&TB_iframe=true&height=500&width=800')
machine.add_transition ( trigger = 'Information', source = '詹世煌', dest = 'http://www.stat.ncku.edu.tw/UserFunc/ProfData/UserShowProfessor.asp?pid=7806003&keepThis=true&TB_iframe=true&height=500&width=800')
machine.add_transition ( trigger = 'Information', source = '趙昌泰', dest = 'http://www.stat.ncku.edu.tw/UserFunc/ProfData/UserShowProfessor.asp?pid=8808043&keepThis=true&TB_iframe=true&height=500&width=800')
machine.add_transition ( trigger = 'Information', source = '鄭順林', dest = 'http://www.stat.ncku.edu.tw/UserFunc/ProfData/UserShowProfessor.asp?pid=9602004&keepThis=true&TB_iframe=true&height=500&width=800')
machine.add_transition ( trigger = 'Information', source = '杜宜軒', dest = 'http://www.stat.ncku.edu.tw/UserFunc/ProfData/UserShowProfessor.asp?pid=9602001&keepThis=true&TB_iframe=true&height=500&width=800')
machine.add_transition ( trigger = 'Information', source = '張升懋', dest = 'http://www.stat.ncku.edu.tw/UserFunc/ProfData/UserShowProfessor.asp?pid=9608012&keepThis=true&TB_iframe=true&height=500&width=800')
machine.add_transition ( trigger = 'Information', source = '李國榮', dest = 'http://www.stat.ncku.edu.tw/UserFunc/ProfData/UserShowProfessor.asp?pid=10108158&keepThis=true&TB_iframe=true&height=500&width=800')
machine.add_transition ( trigger = 'Information', source = '蘇佩芳', dest = 'http://www.stat.ncku.edu.tw/UserFunc/ProfData/UserShowProfessor.asp?pid=10208102&keepThis=true&TB_iframe=true&height=500&width=800')
machine.add_transition ( trigger = 'Information', source = '林良靖', dest = 'http://www.stat.ncku.edu.tw/UserFunc/ProfData/UserShowProfessor.asp?pid=10402001&keepThis=true&TB_iframe=true&height=500&width=800')
machine.add_transition ( trigger = 'Information', source = '張欣民', dest = 'http://www.stat.ncku.edu.tw/UserFunc/ProfData/UserShowProfessor.asp?pid=10402006&keepThis=true&TB_iframe=true&height=500&width=800')
machine.add_transition ( trigger = 'Information', source = '李俊毅', dest = 'http://www.stat.ncku.edu.tw/UserFunc/ProfData/UserShowProfessor.asp?pid=10408028&keepThis=true&TB_iframe=true&height=500&width=800')
machine.add_transition ( trigger = 'Information', source = '李政德', dest = 'http://www.stat.ncku.edu.tw/UserFunc/ProfData/UserShowProfessor.asp?pid=10508029&keepThis=true&TB_iframe=true&height=500&width=800')
machine.add_transition ( trigger = 'Information', source = '李宜真', dest = 'http://www.stat.ncku.edu.tw/UserFunc/ProfData/UserShowProfessor.asp?pid=10608025&keepThis=true&TB_iframe=true&height=500&width=800')
machine.add_transition ( trigger = 'Information', source = '曾仲瑩', dest = 'http://www4.stat.ncsu.edu/~jytzeng/index.php')
machine.add_transition ( trigger = 'Information', source = '楊欣洲', dest = 'http://www.stat.sinica.edu.tw/hsinchou/')
machine.add_transition ( trigger = 'Information', source = '吳致杰', dest = 'http://ph.med.ncku.edu.tw/?menu=teacher_more&id=36&kind=teacher2')
machine.add_transition ( trigger = 'Information', source = '吳鐵肩', dest = 'http://www.stat.ncku.edu.tw/UserFunc/ProfData/UserShowProfessor.asp?pid=8902003&keepThis=true&TB_iframe=true&height=500&width=800')
machine.add_transition ( trigger = 'Information', source = '呂金河', dest = 'http://www.stat.ncku.edu.tw/UserFunc/ProfData/UserShowProfessor.asp?pid=6602001&keepThis=true&TB_iframe=true&height=500&width=800')
machine.add_transition ( trigger = 'Information', source = '張紹洪', dest = 'http://www.sta.cuhk.edu.hk/shcheung')
machine.add_transition ( trigger = 'Information', source = '吳宗正', dest = 'http://www.stat.ncku.edu.tw/UserFunc/ProfData/UserShowProfessor.asp?pid=6208020&keepThis=true&TB_iframe=true&height=500&width=800')
machine.add_transition ( trigger = 'Information', source = '許秀麗', dest = 'http://www.stat.ncku.edu.tw/UserFunc/ProfData/UserShowProfessor.asp?pid=7808051&keepThis=true&TB_iframe=true&height=500&width=800')
machine.add_transition ( trigger = 'Information', source = '鄭碧娥', dest = 'http://www.stat.ncku.edu.tw/UserFunc/ProfData/UserShowProfessor.asp?pid=7308041&keepThis=true&TB_iframe=true&height=500&width=800')
machine.add_transition ( trigger = 'Information', source = '程毅豪', dest = 'http://www.stat.sinica.edu.tw/yhchen/')

def _set_webhook():
    status = bot.set_webhook ( WEBHOOK_URL )
    if not status:
        print ( 'Webhook setup failed' )
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format ( WEBHOOK_URL ) )

@app.route('/hook', methods = ['POST'] )
def webhook_handler():
    update = telegram.Update.de_json ( request.get_json( force = True ), bot )
    machine.advance ( update )
    return 'ok'

@app.route('/show-fsm', methods = ['GET'] )
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw ( byte_io, prog = 'dot', format = 'png' )
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename = 'fsm.png', mimetype = 'image/png' )

if __name__ == "__main__":
    _set_webhook()
    app.run()