import stomp
import time
import sys

class MyListener(stomp.ConnectionListener):
    msg_list = []

    def __init__(self):
        self.msg_list = []

    def on_message(self, frame):
        print(frame.body)
        
#nawiazanie polaczenia z brokerem
c = stomp.Connection([('localhost', 61613)])
c.set_listener('', MyListener())
c.connect('admin', 'password', wait=True)

#podlaczenie do kolejki
c.subscribe('Projekt', '1',)

#oczekiwanie na komunikat i rozlacznenie polaczenia z brokerem
time.sleep(100000)
c.disconnect()



