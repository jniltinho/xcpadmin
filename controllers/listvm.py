# coding: utf8
# tente algo como


from XCP import xcp_data

def index():
    response.title = "XCP ADMIN"
    vm_list = xcp_data(url='192.168.20.192', password='123456')
    
    return dict(table=vm_list)
    
    
def get_data():
    vm_list = xcp_data(url='192.168.20.192', password='123456')
    return response.json(str(vm_list))
