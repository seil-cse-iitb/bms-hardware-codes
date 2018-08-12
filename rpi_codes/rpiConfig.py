'''
Rpi Config
'''

# MQTT DETAILS
mqttHost='10.129.149.9'
mqttPort=1883
mqttKeepalive=60
# mqttTopicName='action/SEIL/Appliance_Test/0'
mqttTopicName = 'actuation/kresit/2/213/#'
#'action/SEIL/Applaince/1/'
'''
# DATABASE DETAILS
dbHost = 'chanakya.seil.cse.iitb.ac.in'
dbReader = 'root'
dbWriter = 'root'
dbPassword = 'root'
dbDatabase = 'datapool'
tblCurrentStatus = 'portal_appliancestatus'
tblLogChange = 'portal_actions'
'''

# DATABASE DETAILS
dbHost = 'chanakya.seil.cse.iitb.ac.in'
dbReader = 'admin'
dbWriter = 'admin'
dbPassword = 'letmein'
dbDatabase = 'app_portal'
tblCurrentStatus = 'portal_appliancestatus'
tblLogChange = 'portal_actions'


# DICT OF LIST OF APPLIANCES
appList={"app1":'L',"app2":'F'}
