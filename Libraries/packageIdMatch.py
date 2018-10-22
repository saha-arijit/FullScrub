import csv
from datetime import datetime
import validation
import readConfig
import Send_email


def create_csv():

	config_File = readConfig.readConfig()#This will read the config file and return the values in a dict

	emails = config_File['AdminEmail'].split(',')

	result = validation.validate(emails)

	if (result == True):
		print ("Execution will proceed.")
		parseWrite(config_File)
	else:
		print ("Execution stopped.")

def parseWrite(config_File):

	#This will read the Master file and take the Values from
	masterFile = open('./inputfiles/' + config_File['tcsInputFile'],'r+')
	masterreader = csv.reader(masterFile)

	rowNo = 0
	headerSplit = []
	contentList = []

	for row in masterreader:
		if rowNo == 0:
			# This will get the Header values....
			headerRow = row[0]
			headerSplit = headerRow.split('|')
			for i in range (0,len(headerSplit)):
				if(headerSplit[i] == 'PackageId'):
					PackageId_row = i
				if(headerSplit[i] == 'ContractId'):
					ContractId_row = i
				if(headerSplit[i] == 'ProductId'):
					ProductId_row = i
				if(headerSplit[i] == 'Title'):
					title_row = i
				if(headerSplit[i] == 'LicenseStart'):
					LicenseStart_row = i
				if(headerSplit[i] == 'LicenseEnd'):
					LicenseEnd_row = i 
				if(headerSplit[i] == 'Duration'):
					tcsduration_row = i 
				if(headerSplit[i] == 'VCMAssetID'):
					VCMAssetID_row = i 
				if(headerSplit[i] == 'FIBEAssetID'):
					FIBEAssetID_row = i 
				if(headerSplit[i] == 'VSPPAssetID'):
					VSPPAssetID_row = i  
				if(headerSplit[i] == 'IPVODAssetID'):
					IPVODAssetID_row = i
			
		else:
			finalRow = ''
			for element in row:
				finalRow = finalRow+element
				#finalRow = compilation of single row						
			contentList.append(finalRow)

		rowNo = rowNo + 1

	inputfil_rowNo = rowNo


	#This will read the first Input file and take the providerassetid 
	fibeAssest = open('./inputfiles/' + config_File['FIBEInputFile'],'r')
	reader1 = csv.reader(fibeAssest)

	rowNo1 = 0
	headerSplit1 = []
	PSI_List1 = []

	for row in reader1:
		if rowNo1 == 0:
			headerRow = row
			headerSplit1 = headerRow[0].split('|')
			for i in range(0,len(headerSplit1)):
				if (headerSplit1[i] == 'providerassetid'):
					providerassetid_row = i
		else:
			PSI = row[0].split('|')[providerassetid_row]   

			PSI_List1.append(PSI)

		rowNo1 = rowNo1 + 1

	#This will read the second Input file and take the providerassetid 
	aliantAssest = open('./inputfiles/' + config_File['AliantInputFile'],'r')
	reader2 = csv.reader(aliantAssest)

	rowNo2 = 0
	headerSplit2 = []
	PSI_List2 = []

	totalcount = 0

	for row in reader2:
		if rowNo2 == 0:
			headerRow = row
			headerSplit2 = headerRow[0].split('|')
			for i in range(0,len(headerSplit2)):
				if (headerSplit2[i] == 'providerassetid'):
					aliant_row = i
		else:
			PSI = row[0].split('|')[aliant_row]
			PSI_List2.append(PSI)

		rowNo2 = rowNo2 + 1

	#This will read the third Input file and take the assetId and msdId 
	vcmReport = open('./inputfiles/' + config_File['VCMInputFile'],'r')
	reader3 = csv.reader(vcmReport)

	rowNo3 = 0
	headerSplit3 = []
	vcm_List = []

	for row in reader3:
		if rowNo3 == 0:
			headerRow3 = row
			for i in range(0,len(headerRow3)):
				if (headerRow3[i] == 'assetId'):
					vcmReport_row = i
				if (headerRow3[i] == 'vcmPackageId'):
					vcmReport_value = i
				if (headerRow3[i] == 'categories'):
					vcmReport_categories = i
				if (headerRow3[i] == 'azukiIngestionState'):
					vcmReport_azukiIngestionState = i
		else:
			vcm_List.append(row)

		rowNo3 = rowNo3 + 1

	#This will read the fourth Input file and take the tcsMasterId and vssAssetId 
	vssaFile = open('./inputfiles/' + config_File['VSSAInputFile'],'r')
	reader4 = csv.reader(vssaFile)

	rowNo4 = 0
	headerSplit4 = []
	vssa_List = []

	for row in reader4:
		if rowNo4 == 0:
			headerRow4 = row
			for i in range(0,len(headerRow4)):
				if (headerRow4[i] == 'vssAssetId'):
					vssa_row = i
		else:
			vssa_List.append(row)

		rowNo4 = rowNo4 + 1

	#This will read the fifth Input file and take the ID and providerId
	ipvodFile = open('./inputfiles/' + config_File['IPVODInputFile'],'r+')

	rowNo5 = 0
	headerSplit5 = []
	ipvod_List = []

	for row in ipvodFile:
		if rowNo5 == 0:
			headerRow5 = row
			headerSplit5 = headerRow5.split('|')
			for i in range (0,len(headerSplit5)):
				if(headerSplit5[i] == 'ID'):
					ipvod_row = i
				if(headerSplit5[i] == 'AssetID'):
					ipvod_value = i	
		else:
			ipvod_List.append(row)

		rowNo5 = rowNo5 + 1

	#This will read the sixth Input file and take the contractId and providerId
	contractFile = open('./Libraries/list_contract_provider','r+')
	reader6 = csv.reader(contractFile)
	contract_List = []

	for row in reader6:
		contract_List.append(row[0])

	#This will read the seventh Input file and take the contractId and priority
	contractFile = open('./Libraries/prioritymapping.csv','r+')
	reader7 = csv.reader(contractFile)

	rowNo7 = 0
	headerSplit7 = []
	mapping_List = []

	for row in reader7:
		if rowNo7 == 0:
			headerRow7 = row[0]
			headerSplit7 = headerRow7.split('|')
			for i in range (0,len(headerSplit7)):
				if(headerSplit7[i] == 'contractid'):
					mapping_row = i
				if(headerSplit7[i] == 'priority'):
					mapping_value = i	
		else:
			mapping_List.append(row[0])

		rowNo7 = rowNo7 + 1


	InvalidContract_File = open('./inputfiles/InvalidContract.txt','r+')

	InvalidContract_List = []

	for row in InvalidContract_File:
		InvalidContract_List.append(row)

	ContractOverride_File = open('./inputfiles/ContractOverride.txt','r+')

	ContractOverride_List = []

	for row in ContractOverride_File:
		ContractOverride_List.append(row)


	#This is the output file
	csvFile = open('./outputfiles/outputfile.csv','w')
	writer = csv.writer(csvFile)

	outputfile_rowNo = 1

	#Headers of output file
	writer.writerow(['prodid','TCSassetid','FIBEAssetID','vcmassetid','FONSEAssetID','IPVODAssetID','title','providContractId','contract','licensestart','licenseEnd','PriorityContractId','Future','FIBE','ALIANT','FONSE','IPVOD','VCM','VSPP','categories','tcsduration','Valid Contract','Valid Asset','Ingestion State'])


	#This part will iterate through all files and match master file's packageId and ContractId with other files elements
	for content in contentList:

		#Values from Master File
		ProductId    = content.split('|')[ProductId_row]
		PackageId    = content.split('|')[PackageId_row]
		ContractId   = content.split('|')[ContractId_row]
		title        = content.split('|')[title_row]
		LicenseStart = content.split('|')[LicenseStart_row]
		LicenseEnd   = content.split('|')[LicenseEnd_row]
		tcsduration  = content.split('|')[tcsduration_row]
		VCMAssetID   = content.split('|')[VCMAssetID_row]
		FIBEAssetID  = content.split('|')[FIBEAssetID_row] 
		VSPPAssetID  = content.split('|')[VSPPAssetID_row]
		IPVODAssetID = content.split('|')[IPVODAssetID_row]

		InvalidContract_Value = '' 
		for value in InvalidContract_List:
			if ContractId in value:
				InvalidContract_Value = 'NO'

		ContractOverride_Value = ''
		for value in ContractOverride_List:
			if ProductId in value:
				ContractOverride_Value = 'NO'

		if InvalidContract_Value == 'NO':
			element = [ProductId,PackageId,PackageId,'N/A','N/A','N/A',title,'N/A',ContractId,LicenseStart,LicenseEnd,'N/A',Future,'','','','','','','',tcsduration,'NO','','N/A']
		
		elif ContractOverride_Value == 'NO':
			element = [ProductId,PackageId,PackageId,'N/A','N/A','N/A',title,'N/A',ContractId,LicenseStart,LicenseEnd,'N/A',Future,'','','','','','','',tcsduration,'YES','NO','N/A']
		
		else:
			#Values from input files
			FibeValue   = ''
			AliantValue = ''
			VCM_Value   = ''
			VsspValue   = ''
			IPVOD_value = ''
			categories  = ''
			azukiIngestionState = ''
			ipvod_assetValue    = ''

			providContractId   = ''
			PriorityContractId = ''

			for PSI1 in PSI_List1:
				if FIBEAssetID == PSI1:#matching FIBEAssetID with providerAssetId
					FibeValue = PSI1

			for PSI2 in PSI_List2:
				if FIBEAssetID == PSI2:#matching FIBEAssetID with providerAssetId
					AliantValue = PSI2

			for vcm in vcm_List:
				if PackageId == vcm[vcmReport_row]:#matching packageId vcmAssetId
					categories = vcm[vcmReport_categories]
					azukiIngestionState = vcm[vcmReport_azukiIngestionState]
					VCM_Value  = vcm[vcmReport_value]				

			for vssa in vssa_List:
				if VSPPAssetID == vssa[vssa_row]:#matching VSPPAssetID
					VsspValue = vssa[vssa_row]

			for ipvod in ipvod_List:
				ipvod = ipvod.split('|')
				if PackageId == ipvod[ipvod_row]:
					ipvod_assetValue = ipvod[ipvod_value]
				if IPVODAssetID == ipvod[ipvod_value]:#matching IPVODAssetID
					IPVOD_value = ipvod[ipvod_value]

			for contract in contract_List:
				if ContractId in contract:#matching ContractId
					contract = contract.split('|')
					providContractId = contract[1]

			for mapping in mapping_List:
					mapping = mapping.split('|')
					if ContractId == mapping[mapping_row]:#matching ContractId
						PriorityContractId = mapping[mapping_value]

			if FibeValue == '':#For FIBE
				Fibe = 'NO'
			else:
				Fibe = 'YES'

			if AliantValue == '':#For Aliant
				Aliant = 'NO'
			else:
				Aliant = 'YES'

			if VCM_Value == '':#For VCM
				VCM = 'NO'
			else:
				VCM = 'YES'

			if VsspValue == '':#For VSPP
				VSPP = 'NO'
			else:
				VSPP = 'YES'

			if IPVOD_value == '':#For IPVOD
				IPVOD = 'NO'
			else:
				IPVOD = 'YES'

			if azukiIngestionState == 'FINISHED':#For FONSE
				azukiIngestion_Value = 'YES'
			else:
				azukiIngestion_Value = 'NO'

			LicenseDate = datetime.strptime(LicenseStart, '%Y/%m/%d %H:%M')#For FUTURE
			now = datetime.now()
			if LicenseDate > now:
				Future = 'YES'
			else:
				Future = 'NO'
					
			
			element = [ProductId,PackageId,PackageId,VCM_Value,VSPPAssetID,ipvod_assetValue,title,providContractId,ContractId,LicenseStart,LicenseEnd,PriorityContractId,Future,Fibe,Aliant,azukiIngestion_Value,IPVOD,VCM,VSPP,categories,tcsduration,"YES","YES",azukiIngestionState]

		outputfile_rowNo = outputfile_rowNo + 1
		writer.writerow(element)

	if inputfil_rowNo == outputfile_rowNo:
		pass
	else:
		emails = config_File['AdminEmail'].split(',')
		pass
		# Send_email.send_Email('',emails)