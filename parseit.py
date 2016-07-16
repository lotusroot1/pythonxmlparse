# just testing some stuff w/ python


import os
import sys
import xml.etree.ElementTree as ET

processDir='.'
supportedExtensions=['xml']

if len(sys.argv) > 1: processDir=sys.argv[1]

print 'Will process files from: ', processDir

def isSupportedFile(fileName):
	extension = os.path.splitext(fileName)[1]
	# remove the dot
	extension = extension[1:]
	for ext in supportedExtensions:
		if ext == extension: return True
		else: print 'Extension not supported: ', extension
	return False

def parseFile(fileName):
	if not isSupportedFile(fileName): return 'Unsupported file'
	
	print 'Parsing file: ', fileName
	tree = ET.parse(fileName)
	root = tree.getroot()
	
	for child in root:
		print child.tag, child.attrib
		for attrib in child.attrib:
			print 'attribVal: ', child.get(attrib)

for dirName, subdirList, fileList in os.walk(processDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        # print('\t%s' % fname)
	# print os.path.join(dirName, fname)

	parseFile(os.path.join(dirName, fname))

