def parseJson(data):
	for studyData in data:
		formsData = studyData["Forms"]
		for formData in formsData :
			itemGroup = formData["ItemGroups"]
			for itemGr in itemGroup :
				items = itemGr["Items"]
				for item in items :
					if item["OID"] == "I_DEMOG_DEM_AGE" :
						item["Value"] = int(item["Value"].replace("Years","").strip())  
	return data