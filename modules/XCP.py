#!/usr/bin/env python
# coding: utf8


import sys, time
import XenAPI

  
def xcp_data(url, username='root', password='123456'):
    url = 'http://' + url
    username = username
    password = password
    session = XenAPI.Session(url)
    session.xenapi.login_with_password(username, password)
    vms = session.xenapi.VM.get_all()
    vm_list = {}
    for vm in vms:
        get = session.xenapi.VM.get_record(vm)
        get["memory_static_max"] = str((int(get["memory_static_max"]) / (1024 * 1024)))
        vm_list[vm] = get
    
    return vm_list
