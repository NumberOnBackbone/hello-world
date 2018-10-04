import requests
import datetime

class Rudebot:
    
    def __init__(self, token):
        self.token = token
        self.api_url = 'https://api.telegram.org/bot{}/'.format(token)


    def get_updates(self,offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        response = requests.get(self.api_url + method, params)
        result_json = response.json()['result']
        return result_json

    def send_message(self,chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        response = requests.post(self.api_url + method, params)
        return response

    def get_last_update(self):
        get_result = self.get_updates()
        
        if len(get_result)>0:
            last_update = get_result[-1]
        else
            last_update = get_result[len(get_result)]

        return last_update
        
        

greet_bot = Rudebot(token)
greetings = ('ша, петушандры','сегодня ночуете на параше')
now= datetime.datetime.now()



def main():
    new_offset = None
    today = now.day
    hour = now.hour
    
    while True:
        greet_bot.get_updates(new_offset)

        last_update = greet_bot.get_last_update()
        
        last_update_id = last_update['update_id']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
            greet_bot.send_message(last_chat_id, 'Сранины в этом курятнике тихо')
            today+=1
        elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour <17:
            greet_bot.send_message(last_chat_id, 'Солнце в зените, петухов ебите')
            today+=1

        elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
            greet_bot.send_message(last_chat_id, 'Вечер в хату, опущенцы')
            today+=1

        new_offset = last_update_id +1



if  __name__== '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
