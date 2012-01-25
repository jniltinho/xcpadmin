# coding: utf8
# tente algo como

from XCP import xcp_data

@auth.requires_login()
def index():
    vmrecord = xcp_data(url='192.168.20.192', password='123456')
    
    return dict(table=vmrecord)
    
    
def get_data():
    vmrecord = xcp_data(url='192.168.20.192', password='123456')
    return response.json(str(vmrecord))
