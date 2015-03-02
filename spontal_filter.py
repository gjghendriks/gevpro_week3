'''
Program for for correcting data in an XML file
By Gijs Hendriks
s2410540
'''

import xml.etree.ElementTree as ET
import sys
tree = ET.parse(sys.argv[1])
root = tree.getroot()
spontal = 3
spontal_filtered = 3
for child in root:
    spontal += 2
    for nested in child:
        spontal += 1

for point in root:
    
    if(point.find('BOTTOM_HZ').text > point.find('F0_START').text > point.find('TOP_HZ').text):
        #print(point.find('BOTTOM_HZ').text, point.find('F0_END').text, point.find('F0_START').text, point.find('TOP_HZ').text)
        root.remove(point)
 
    elif(point.find('BOTTOM_HZ').text > point.find('F0_END').text > point.find('TOP_HZ').text):
        #print(point.find('BOTTOM_HZ').text, point.find('F0_END').text, point.find('F0_START').text, point.find('TOP_HZ').text)
        root.remove(point)
        
    
for child in root:
    spontal_filtered += 2
    for nested in child:
        spontal_filtered += 1
tree.write(sys.argv[2], encoding="utf-8", xml_declaration=True)
print (spontal, sys.argv[1])
print (spontal_filtered, sys.argv[2])
print (spontal+spontal_filtered, ' total')

