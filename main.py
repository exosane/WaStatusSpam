import time

from ppadb.client import Client as AdbClient

def connect():
    client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037

    devices = client.devices()

    if len(devices) == 0:
        print('No devices')
        quit()

    device = devices[0]

    print(f'Connected to {device}')

    return device, client

if __name__ == '__main__':
    device, client = connect()

    x = 204
    text_status = '638 1242'
    send_button = '638 780'


    while (x < 1000):

        x = x + 1
        device.shell(f'input tap {text_status}')
        y = f"Stato numero {x}"

        device.shell(f'input text "{y}"')
        device.shell(f'input tap {send_button}')
    pass
