import ajaxFunctions
import time

botId = 0

# Get registration information
print('Bot registration')
buildingId = input('Insert building id: ')
botName = input('Insert bot name: ')

# Send register message
botId = ajaxFunctions.sendRegisterMessage(buildingId, botName)

# Give some time to get building id from ajax request
print('.')
time.sleep(0.3)
print('..')
time.sleep(0.3)
print('...')
time.sleep(0.3)
print('You can now broadcast messages to building with id ' + buildingId)

# Send message infinite loop
while True:
    message = input('Insert broadcast message: ')
    print(ajaxFunctions.sendBroadcastMessage(botId, message))