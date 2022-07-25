import requests

print("""
(1) Use Webhook Spammer
(2) Discord Account Spammer
(3) Exit
""")


user = str(input('Which option would you like to choose: '))

if user == '1':

    url = input('Webhook URL: ')

    msg = input('Enter Message to Spam: ')

    running = True

    while running:

     response1 = requests.post(url = f'{url}',json = {'content':f'{msg}'})

     if response1.status_code == '200':
        print('Spamming')

    
if user == '2':

    url1 = input('Token: ')

    message = input('What you would like to spam: ')

    ChannelID = input('Channel ID you would like to spam in: ')

    header = {'authorization':f'{url1}'}

    payload = {'content' : f'{message}'}

    running = True

    while running:

     response2 = requests.post(url = f'https://discord.com/api/v9/channels/{ChannelID}/messages', headers = header,data = payload)

     if response2.status_code == '200':
         print(f'Spamming')

if KeyboardInterrupt:
    exit()

if user == '3':
    try:
      exit() or KeyboardInterrupt == exit()
    except Exception as e:

        print(f'{e}')

