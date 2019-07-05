from durable.lang import *
import json

from parsing import *

with open('test.json') as json_file:  
    data = json.load(json_file)

    data = parseJson(data)
    FemalePatientCount = 0
    MalePatientCount = 0
with ruleset('studyData'):
    @when_all((m.OID == 'SE_INITIALVISIT') & (m.Forms.anyItem((item.OID =="F_DEMOGRAPHICS_V20") &
     (item.ItemGroups.anyItem((item.OID=="IG_DEMOG_DEMO") &
      (item.Items.anyItem((item.OID == "I_DEMOG_DEM_GEN") & (item.Value =="2"))))))))
    def approvedRule1(c):
    	global FemalePatientCount
    	FemalePatientCount = FemalePatientCount+1
        print ('This event passed successfully for counting female')

    @when_all((m.OID == 'SE_INITIALVISIT') & (m.Forms.anyItem((item.OID =="F_DEMOGRAPHICS_V20") &
     (item.ItemGroups.anyItem(
     	(item.OID=="IG_DEMOG_DEMO") &
      (item.Items.anyItem((item.OID == "I_DEMOG_DEM_GEN") & (item.Value =="1"))) 
       ))))
    &
    (m.OID == 'SE_INITIALVISIT') & (m.Forms.anyItem((item.OID =="F_DEMOGRAPHICS_V20") &
     (item.ItemGroups.anyItem(
     	(item.OID=="IG_DEMOG_DEMO") &
     (item.Items.anyItem((item.OID == "I_DEMOG_DEM_AGE") & (item.Value > 70)))
     ))))
    )
    def approvedRule2(c):
    	global MalePatientCount
    	MalePatientCount = MalePatientCount+1
        print ('This event passed successfully for counting male and his age is more than 70')
            

for studyData in data:
	try:
		post('studyData',studyData)

	except BaseException as e:
		print('This event failed')


print("The number of female patirnt is: {0}".format(FemalePatientCount))

print("The number of male patirnt and his age is more than 70 is: {0}".format(MalePatientCount))

