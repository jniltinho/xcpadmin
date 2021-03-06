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
    vms = session.xenapi.VM.get_all_records()
    vbds = session.xenapi.VBD.get_all_records()
    vdis = session.xenapi.VDI.get_all_records()
    srs = session.xenapi.SR.get_all_records()
    #vms = session.xenapi.VM.get_all()
    session.xenapi.logout()
    vmlist = {}
    for vm in vms:
        vmrec = vms[vm]
        vmrec["memory_static_max"] = str((int(vmrec["memory_static_max"]) / (1024 * 1024)))
        vmlist[vm] = vmrec
    
    return vmlist
