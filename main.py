import pandas
from datetime import datetime
import os
from twilio.rest import Client


def send_sms(trash, tel_number):
    #print(f"odbiór {trash}")
    account_sid = '[Sid]'
    auth_token = '[AuthToken]'
    client = Client(account_sid, auth_token)

    message = client.messages.create(messaging_service_sid='XXXXX',
                                     body=f'Jutro odbiór {trash}, nie zapomnij o wystawieniu worków 🗑️',
                                     from_='twilio_number',
                                     to=tel_number
                                     )
    print(message.sid)


number_lists = ['tel_number_1', '+tel_number_2']
data = pandas.read_csv("data.csv")
current_month = datetime.now().month
current_day = datetime.now().day

trash_data_frame = pandas.DataFrame(data)
this_month_schedule = trash_data_frame.loc[current_month-1]
#change multiple days to list with "," delimiter
mixed_schedule = this_month_schedule['mixed'].split(",")
for item in mixed_schedule:
    if int(item)-1 == current_day:
        trash_type = "NIESEGREGOWALNE"
        for number in number_lists:
            send_sms(trash_type, number)
if this_month_schedule['plastic']-1 == current_day:
    trash_type = "PLASTIK"
    for number in number_lists:
        send_sms(trash_type, number)
if this_month_schedule['paper']-1 == current_day:
    trash_type = "PAPIER"
    for number in number_lists:
        send_sms(trash_type, number)
if this_month_schedule['glass']-1 == current_day:
    trash_type = "SZKLO"
    for number in number_lists:
        send_sms(trash_type, number)
if this_month_schedule['tyres']-1 == current_day:
    trash_type = "OPONY"
    for number in number_lists:
        send_sms(trash_type, number)
if this_month_schedule['dangerous']-1 == current_day:
    trash_type = "ODPADY NIEBEZPIECZNE"
    for number in number_lists:
        send_sms(trash_type, number)
