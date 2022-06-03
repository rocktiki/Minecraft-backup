#!/usr/bin/python
#
# Custom Minecraft Backup
# Sean Hawthorne
#
# Objective: Backup Select (TRIMMED) Regions of a minecraft world and the accompanying files 
#

# imports
import os
import json

# functions
def getdircontents(dirname):
	dirtmp = [ config['world_name']+"/"+dirname+"/"+f for f in os.listdir(config['saves_path']+"/"+config['world_name']+"/"+dirname) if os.path.isfile(os.path.join(config['saves_path']+"/"+config['world_name']+"/"+dirname,f)) ] 
	return dirtmp

#======================================
# Read in JSON configuration file (backup.json)
# Contains var:backup_path var:world_path arr:DIM0 arr:DIM1 arr:DIM-1
with open("backup.json","r") as file:
	config = json.load(file)
file.close	
### Test view json contents
if config['debugz']: print (json.dumps(config,indent=4))
#print (config['DIM0'][0])

#======================================
# Create arr:base-files 
## world
base_files = getdircontents("/")
## world/advancements
base_files += getdircontents("advancements")
## world/datapacks
base_files += getdircontents("datapacks")
## world/playerdata
base_files += getdircontents("playerdata")
## world/stats
base_files += getdircontents("stats")
### Test view base_files contents
if config['debugz']: print(*base_files, sep = "\n" )

#======================================
# Create arr:dim0-files
## world/data
dim0_files = getdircontents("data")
## world/region
dim0_region = getdircontents("region")
dim0_files += [i for i in dim0_region if any(i for j in config['DIM0'] if str(j) in i)]
## world/entities
dim0_entities = getdircontents("entities")
dim0_files += [i for i in dim0_entities if any(i for j in config['DIM0'] if str(j) in i)]
## world/poi
dim0_poi = getdircontents("poi")
dim0_files += [i for i in dim0_poi if any(i for j in config['DIM0'] if str(j) in i)]
### Test view dim0_files contents
if config['debugz']: print(*dim0_files, sep = "\n" )

# Create arr:dim1-files
## world/DIM1/data
dim1_files = getdircontents("DIM1/data")
## world/DIM1/region
dim1_region = getdircontents("DIM1/region")
dim1_files += [i for i in dim1_region if any(i for j in config['DIM1'] if str(j) in i)]
## world/DIM1/entities
dim1_entities = getdircontents("DIM1/entities")
dim1_files += [i for i in dim1_entities if any(i for j in config['DIM1'] if str(j) in i)]
## world/DIM1/poi
dim1_poi = getdircontents("DIM1/poi")
dim1_files += [i for i in dim1_poi if any(i for j in config['DIM1'] if str(j) in i)]
### Test view dim0_files contents
if config['debugz']: print(*dim1_files, sep = "\n" )

# Create arr:dim-1-files
## world/DIM-1/data
dim_1_files = getdircontents("DIM-1/data")
## world/DIM-1/region
dim_1_region = getdircontents("DIM-1/region")
dim_1_files += [i for i in dim_1_region if any(i for j in config['DIM-1'] if str(j) in i)]
## world/DIM-1/entities
dim_1_entities = getdircontents("DIM-1/entities")
dim_1_files += [i for i in dim_1_entities if any(i for j in config['DIM-1'] if str(j) in i)]
## world/DIM-1/poi
dim_1_poi = getdircontents("DIM-1/poi")
dim_1_files += [i for i in dim_1_poi if any(i for j in config['DIM-1'] if str(j) in i)]
### Test view dim0_files contents
if config['debugz']: print(*dim_1_files, sep = "\n" )

# get date

# Write list of files to (date)-waybill.lst


# Use backup-waybill.tmp to make (date)-waybill.md5
# Add backup backup.py/backup.json/(date)-waybill.tmp/(date)-waybill.md5 to (date)-waybill.tmp
### Quiesce Minecraft?
# Use tar to make compressed archive using backup-waybill.tmp
### Engage Minecraft?
### Notification?
