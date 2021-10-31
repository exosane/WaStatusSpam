import time

from ppadb.client import Client as AdbClient

def connect():
    client = AdbClient(host="127.0.0.1", port=5037) #Default is "127.0.0.1" and 5037

    devices = client.devices()

    if len(devices) == 0:
        print('No devices')
        quit()

    device = devices[0]

    print(f'Connected to {device}')

    return device, client

if __name__ == '__main__':
    device, client = connect()

    #Put here the text that you want to spam in your status
    text = "Hello your computer have a virus"
    #Put here the number of statuses
    status = 1000
    #Coordinates of the 'Text Status' button in WA (x, y)
    text_status = '638 1242'
    # Coordinates of the 'Send Button' button in WA (x, y)
    send_button = '638 780'

    import time

from ppadb.client import Client as AdbClient

def connect():
    client = AdbClient(host="127.0.0.1", port=5037) #Default is "127.0.0.1" and 5037

    devices = client.devices()

    if len(devices) == 0:
        print('No devices')
        quit()

    device = devices[0]

    print(f'Connected to {device}')

    return device, client

if __name__ == '__main__':
    device, client = connect()

    #Put here the text that you want to spam in your status
    text = "Hello your computer have a virus"
    #Put here the number of statuses
    status = 1000
    
    
    x = 0

    #Coordinates of the 'Text Status' button in WA (x, y)
    text_status = '638 1242'
    # Coordinates of the 'Send Button' button in WA (x, y)
    send_button = '638 780'


    while (x < status):

        x = x + 1
        
        device.shell(f'input tap {text_status}')
        
        y = f"{text}" #If you want to add a number after the text, add {x}. Ex: Status 1, Status 2, etc...

        device.shell(f'input text "{y}"')
        device.shell(f'input tap {send_button}')
    pass


    while (x < status):

        x = x + 1
        
        device.shell(f'input tap {text_status}')
        
        y = f"{text}" #If you want to add a number after the text, add {x}. Ex: Status 1, Status 2, etc...

        device.shell(f'input text "{y}"')
        device.shell(f'input tap {send_button}')
    pass
