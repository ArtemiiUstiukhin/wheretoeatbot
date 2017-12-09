import telebot
import requests
import psycopg2

access_token = '502764849:AAEXKT0HdJ3bxjJ40xn3CEg9rhUOSvc5968'

# Создание бота с указанным токеном доступа
bot = telebot.TeleBot(access_token)
chat_id = '@petrakov1bot'

dbhost='ec2-54-247-123-130.eu-west-1.compute.amazonaws.com'
dbdatabase='dbmc7av4l8lh64'
dbuser='naidfjktoihxdk'
dbpassword='b868664b06b5d9a6e1b363a815c183460f4f07f17562062ee0f54d81657807f7'


@bot.message_handler(commands=['all'])
def test_connection(message):
    conn = psycopg2.connect(host=dbhost,database=dbdatabase, user=dbuser, password=dbpassword)
    query = 'SELECT * FROM places LIMIT 100'
    cur = conn.cursor()
    cur.execute(query)
    # bot.send_message(message.chat.id, "The number of parts: " + cur.rowcount)
    row = cur.fetchone()
    print(message.chat.id)
    while row is not None:
        bot.send_message(message.chat.id, '📍' + row[1] + '\n' + row[3])
        
        # print(row)
        row = cur.fetchone()
    cur.close()

# Бот будет отвечать только на текстовые сообщения
@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, '📍 Юля любит ' + message.text)

@bot.message_handler(content_types=['location'])
def send_place(message):
    print(message.chat.id)    
    bot.send_message(message.chat.id, '📍 Деловая Колбаса')
    bot.send_message(message.chat.id, message.location)
    bot.send_location(message.chat.id, '59.9606151', '30.3061886')
    place = (59.9606151,30.3061886)
    client = (message.location.longitude,message.location.latitude)
    distance = compute_distance(place,client)
    bot.send_message(message.chat.id, count_distance(59.9606151,30.3061886,message.location.longitude,message.location.latitude))
    # url = 'http://makeitreal.studio/telegram/get.php'
    # response = requests.get(url)
    # bot.send_message(message.chat.id, response.text)
    

def count_distance(My_longitude, My_latitude, Place_longitude, Place_latitude):
    return Math.sqrt(Math.pow(My_longitude-Place_longitude,2)+Math.pow(My_latitude-Place_latitude,2))
    
    
if __name__ == '__main__':
     bot.polling(none_stop=True)
