#!/usr/bin/env python



import XenAPI
##from tunnel import Tunnel
from tunnel import *
from os import system 


session = XenAPI.Session('http://192.168.20.192')
session.login_with_password('root', '123456')
print session._session


location = 'https://192.168.20.192/console?ref=OpaqueRef:b9a8c558-4c97-5409-df50-d9b6158eaca7'

tunnel = Tunnel(session._session, location)
port = tunnel.get_free_port()
print port
Thread(target=tunnel.listen, args=(port,)).start()


vnc_cmd = "vncviewer localhost::%s" %(str(port))
system(vnc_cmd)


## Para fechar o tunnel
tunnel.close()

                            
                            

