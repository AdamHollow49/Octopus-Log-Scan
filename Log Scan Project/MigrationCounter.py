# This script is designed to take property log lines from a migration log and \
# export them to a CSV.
# As with all automation scripts, be aware there is a chance the script may \
# not work 100% accurately. It's a good idea to verify the data from this \
# scripts output should you decide to use it.

# CSV export will save to the location the script is run from.

#imports
import matplotlib.pyplot as plt
import numpy as np
import csv

#Path to log file
log_path = ""

#List of Properties
prop_list = {'Account': 0,'ActionTemplate': 0,'ApiKey': 0,'Artifact': 0,'Channel': 0,'CommunityActionTemplate': 0,'ActionTemplateVersion': 0,'ExtensionConfiguration': 0, \
'DashboardConfiguration': 0,'DeploymentEnvironment': 0,'DeploymentProcess': 0,'Feed': 0,'LibraryVariableSet': 0,'Lifecycle': 0,'DeploymentTarget': 0, \
'Project': 0,'ProjectTrigger': 0,'ProjectGroup': 0,'Release': 0,'Team': 0,'ScopedUserRole': 0,'Space': 0,'User': 0,'UserRole': 0,'ProjectVariables': 0,'LibraryVariables': 0, \
'Event': 0,'Deployment': 0,'Tenant': 0,'TenantVariable': 0,'Worker': 0,'WorkerPool': 0,'Runbook': 0,'RunbookProcess': 0,'RunbookSnapshot': 0,'RunbookRun': 0,'ServerTask': 0}

#line counter
def count_lines():
	text = open(log_path, "r")
	line_count = 0
	for line in text:
		if line != "\n":
			line_count += 1
	text.close()
	return(line_count)

#check for properties
def scan_lines(property, line_count):
	text = open(log_path, "r")
	counter = 0
	prop_delta = 49 + len(property) #property delta - character count difference between property start on log line and property end on log line
	for line in text:
		prop_slice = line[49:prop_delta] #search for presence of property in line from point of entry:length of property parameter
		if prop_slice == property:
			counter += 1
	text.close()
	prop_list[property] = counter
	return(counter)

def print_results():
	for prop in prop_list:
		print("There are {x} {y} log lines".format(x=scan_lines(prop, count_lines()), y=prop))

def create_csv():
	a_file = open("MigrationCounterResults.csv", "w")
	writer = csv.writer(a_file)
	writer.writerow(['Log Type', 'Number of Lines'])
	for key, value in prop_list.items():
	    writer.writerow([key, value])

	a_file.close()


print("Scanning Log File.")
print("There are {x} lines to scan.".format(x=count_lines()))
print_results()
create_chart()
