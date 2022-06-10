from time import sleep
from marionette_driver import By
from marionette_driver.marionette import Marionette
import datetime
import requests
import winsound
from tqdm import trange

def soundAlert(time:int):
	print("refreshing will resume after the countdown ends")
	for _ in trange(time):
		winsound.Beep(600, 900)

def dateParser(date):
    dateObj = datetime.datetime.strptime(date + " 2022", "%B %d %Y")
    return dateObj.strftime("%y%m%d")

def getDate(client):
    client.refresh()
    sleep(1)
    date = client.execute_script(''' 
    return document.querySelector("div").querySelector(".date-secondary").innerText
    ''')
    return date

def CDC_sendtext(bot_message, chatid): 
	bot_token = ''
	bot_chatID = chatid 
	send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=HTML&text=' + bot_message
	response = requests.get(send_text)
	return response.json()


def reserveJS(client,info):
	reserveJS = """
const firstName = arguments[0]
const lastName = arguments[1]
const hp = arguments[2]
const email = arguments[3]
let a = document.querySelector("div.form-inline")
a.querySelector("label").click()
const promise = new Promise ((resolve, reject) => {
    setTimeout( () => { 
        a.querySelector("a").click();
        resolve();
        }, 1500);
})

promise.then(()=>{
    document.querySelector("input#first-name").value=firstName
    document.querySelector("input#last-name").value=lastName
    document.querySelector("input#phone").value=hp
    document.querySelector("input#email").value=email
})
	"""
	client.execute_script(reserveJS,info)

firstName = "123"
lastName = "456"
hp = 1234567
email = "456@yahoo.com"
info = [firstName,lastName,hp,email]

url = "website"
intTargetDate = 220624 #YYMMDD

client = Marionette(host='localhost', port=2828)
client.start_session()
client.navigate(url)

try:
    while 1:
        dateStringFetched = getDate(client)
        intDateCurrent =  int( dateParser(dateStringFetched) ) #YYMMDD
        print(f"{intDateCurrent} {datetime.datetime.now().strftime('%H:%M:%S')}")
        if intDateCurrent <= intTargetDate:
            datefound = datetime.datetime.strptime(str(intDateCurrent), "%y%m%d")
            reserveJS(client,info)
            msg = "date found at " + datefound.strftime("%d %b %y %a")
            CDC_sendtext(msg,"123456")
            soundAlert(5)
        sleep(120)
except TypeError as e:
    print(e)
    CDC_sendtext("error for marionette","123456")