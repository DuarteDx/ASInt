import ajaxFunctions
import time

botId = 0

# Get registration information
print('Bot registration')
buildingId = input('Insert building id: ')
botName = input('Insert bot name: ')

# Send register message
# ToDo: pass and update botId in ajax request
ajaxFunctions.sendRegisterMessage(buildingId, botName)

# Give some time to get building id from ajax request
print('.')
time.sleep(0.3)
print('..')
time.sleep(0.3)
print('...')
time.sleep(0.3)

# Send message infinite loop
while True:
    message = input('Broadcast message to building ' + buildingId + ': ')
    print(ajaxFunctions.sendBroadcastMessage(botId, message))