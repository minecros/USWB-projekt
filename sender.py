import stomp

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

#wyslanie wiadomosci do kolejki
c.send('Projekt', 'Testowa wiadomosc')
#rozlacznenie polaczenia z brokerem
c.disconnect()
