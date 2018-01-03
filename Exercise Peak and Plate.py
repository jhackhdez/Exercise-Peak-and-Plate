#-*- coding: utf-8 -*-
# Name and Lastname: Ing. Jorge Hernández Roselló

import sys
from datetime import datetime, time

print("-----THIS PROGRAM WILL INDICATE WHETHER YOUR VEHICLE CAN CIRCULATE OR NOT AT THE DATE AND TIME INDICATED BY YOU\
	FOLLOWING THE PEAK AND PLATE LAW IN ECUADOR-----")

plate=str(input("\nPlease, enter your license plate number. Ex. XXX-000 or XXX-0000: "))

date=str(input("\nPlease, enter the date in the specified format:. Ex. DD/MM/YYYY: "))

time=str(input("\nPlease, enter a time in the specified format. Ex. 07:40 or 19:00. "))


class Validator():
	"""Class in charge of the validation of the data entered by the user"""
	
	def __init__(self, p, d, t):
		"""Constructor of the class where declarate the necessary attributes for the creation of the instances of the class"""

		self.plate_in=p
		self.date_in=d
		self.time_in=t

	def validate(self):
		"""Method responsible for validating the correct format of the data entered by the user"""

		if((len(self.plate_in)==7 or len(self.plate_in)==8) and self.plate_in[3]=="-"):
			if(len(self.date_in)==10 and self.date_in[2]=="/" and self.date_in[5]=="/"):
				if(len(self.time_in)==5 and self.time_in[2]==":"):
					print("\n----------------------------------------------------------------------------")
					print("\nThe data entered by you are: \n")
					print("- License Plate Number:" ,self.plate_in.upper(), "\n")
					print("- Date:", self.date_in, "\n")
					print("- Time:", self.time_in, "\n")
				else:
					print("\nThe time entered does not comply with the required format. ")
					sys.exit()
			else:
				print("\nThe date entered does not comply with the required format. ")
				sys.exit()
		else:
			print("\nThe license plate number registration is not correct.")
			sys.exit()

		
class Predictor(Validator):
	"""Class responsible for verifying if a vehicle can transit or not"""

	def prediction(self):
		"""Method where are define the algorithm and dependencies needed to verify if the vehicle can transit or not"""

		time1 = datetime.strptime("07:00:00", "%X").time() 
		time2 = datetime.strptime("09:30:00", "%X").time()
		time3 = datetime.strptime("16:00:00", "%X").time() 
		time4 = datetime.strptime("19:30:00", "%X").time()
		full_time = self.time_in + ":00"
		entry_time = datetime.strptime(full_time, "%X").time()
		"""Definition of time restrictions, as well as the user's time of entry."""

		date_split = self.date_in.split('/')
		try:
			entry_date = datetime(int(date_split[2]), int(date_split[1]), int(date_split[0]), 0, 0, 0)
		except ValueError:
			print("\nThe date entered does not comply with the required format.")
			sys.exit()
		weekday = entry_date.strftime("%a")
		"""Conversion of the time entered to datetime object"""


		if(weekday=="Mon" and (self.plate_in[-1]=="1" or self.plate_in[-1]=="2")):
			if((time1<=entry_time and entry_time<=time2) or (time3<=entry_time and entry_time<=time4)):
				print("***We are sorry but, unfortunately your vehicle can not travel at this time on the road***")
			else:
				print("***We are pleased to inform you, that your vehicle can travel during this time on the road***")

		elif(weekday=="Tue" and (self.plate_in[-1]=="3" or self.plate_in[-1]=="4")):
			if((time1<=entry_time and entry_time<=time2) or (time3<=entry_time and entry_time<=time4)):
				print("***We are sorry but, unfortunately your vehicle can not travel at this time on the road***")
			else:
				print("***We are pleased to inform you, that your vehicle can travel during this time on the road***")

		elif(weekday=="Wed" and (self.plate_in[-1]=="5" or self.plate_in[-1]=="6")):
			if((time1<=entry_time and entry_time<=time2) or (time3<=entry_time and entry_time<=time4)):
				print("***We are sorry but, unfortunately your vehicle can not travel at this time on the road***")
			else:
				print("***We are pleased to inform you, that your vehicle can travel during this time on the road***")

		elif(weekday=="Thu" and (self.plate_in[-1]=="7" or self.plate_in[-1]=="8")):
			if((time1<=entry_time and entry_time<=time2) or (time3<=entry_time and entry_time<=time4)):
				print("***We are sorry but, unfortunately your vehicle can not travel at this time on the road***")
			else:
				print("***We are pleased to inform you, that your vehicle can travel during this time on the road***")

		elif(weekday=="Fri" and (self.plate_in[-1]=="9" or self.plate_in[-1]=="0")):
			if((time1<=entry_time and entry_time<=time2) or (time3<=entry_time and entry_time<=time4)):
				print("***We are sorry but, unfortunately your vehicle can not travel at this time on the road***")
			else:
				print("***We are pleased to inform you, that your vehicle can travel during this time on the road***")

		else:
			print("***We are pleased to inform you, that your vehicle can travel during this time on the road***")
		"""Prediction algorithm"""


#Creating an instance of the Validator object with the corresponding parameters
obj1=Validator(plate,date,time)

#Call the validate method for the validation of the entered parameters
obj1.validate()

#Creating an instance of the Predictor object with the corresponding parameters
obj2=Predictor(plate,date,time)

#Call the prediction method to check if the vehicle can travel on the road or not
obj2.prediction()