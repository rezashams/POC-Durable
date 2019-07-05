from durable.lang import *

output =''
TrialLastExpectedVisit ='tr'
with ruleset('studyData'):

	@when_all(pri(6), (m.ctx.currentVisit.state == 'SE_EOSORLFU') & 
		(m.ctx.currentVisit.CompletionForm.DidPatientComplete == "1") &
		 (m.ctx.Patient.LastCompletedVisit == TrialLastExpectedVisit))
	def detect(c):
		global output
		output = 'Completed'

	@when_all(pri(5), (m.ctx.currentVisit.state == 'SE_EOSORLFU') & 
		(m.ctx.currentVisit.CompletionForm.DidPatientComplete == "1") &
		 (m.ctx.Patient.LastCompletedVisit != TrialLastExpectedVisit))
	def detect(c):
		global output
		output = 'Withdrew'

	@when_all(pri(4), (m.ctx.currentVisit.state == 'SE_EOSORLFU') & 
		(m.ctx.currentVisit.CompletionForm.DidPatientComplete != "1"))
	def detect(c):
		global output
		output = 'Continuing'
   
	@when_all(pri(3), (m.ctx.currentVisit.state == 'INITIAL_VISIT') &
	((m.ctx.currentVisit.InclusionExclusionCriteriaForm.IsPatientEligible == "1")))
	def detect(c):
		global output
		output = 'ScreenSuccess'

	@when_all(pri(2), (m.ctx.currentVisit.state == 'INITIAL_VISIT') &
	((m.ctx.currentVisit.InclusionExclusionCriteriaForm.IsPatientEligible != "1")))
	def detect(c):
		global output
		output = 'ScreenFail'
        
	@when_all(pri(1), (m.ctx.currentVisit.state != 'INITIAL_VISIT') & ((m.ctx.currentVisit.state != 'SE_EOSORLFU')))
	def detect(c):
		global output
		output = 'Continuing'
                


# post('studyData',{'ctx': {"currentVisit" :{'state':'INITIAL_VISIT',
# 	'InclusionExclusionCriteriaForm':{'IsPatientEligible':"1"}} }})
try:
	post('studyData',{'ctx': {"Patient":{"LastCompletedVisit":"tr"},"currentVisit" :{'state':'SE_EOSORLFU',
		'CompletionForm':{"DidPatientComplete":"1"}} }})
	print('output is : {0}'.format(output))
except BaseException as e:
	print('This event failed')
