#!/usr/bin/env python2.6

import zabbix_api
import sys


xmldir = "/vagrant/"
xmlfile = xmldir + sys.argv[1]
zapi = zabbix_api.ZabbixAPI(server='https://10.10.0.2/zabbix', path="", log_level=1)
zapi.login('admin','zabbix')
f = open(xmlfile)
source = f.read()
 
zapi.configuration.import_(
  {
         "format"    :   "xml",
         "rules"     :   {
            "groups" :   {
                  "createMissing"  :  True,
                  "updateExisting" :  True
            },
            "hosts"     :   {
                  "createMissing"   :  True,
                  "updateExisting"  :  True
            },
            "templates" :  {
                  "createMissing"   :  True,
                  "updateExisting"  :  True
             },
             "triggers"  :  {
                  "createMissing"   :  True,
                  "updateExisting"  :  True
             },
             "items"      : {
                  "createMissing"   :   True,
                  "updateExisting"  :   True
             },
             "applications" : {
                  "createMissing"   :   True,
                  "updateExisting"  :   True
             }
          },
          "source" : source
       },
       

  
  )