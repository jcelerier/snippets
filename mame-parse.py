#!/usr/bin/python3

import xml.etree.ElementTree as etree

mamexml = 'mame.xml'

for event, elem in etree.iterparse(mamexml, events=('start', 'end', 'start-ns', 'end-ns')):
  if elem.tag == 'game' and event == 'start':
    rom = elem.attrib['name']
    clone = 'cloneof' in elem.attrib
    working = False

    for child in elem:
      if child.tag == 'description':
        desc = child.text

      if child.tag == 'driver':
        if child.attrib['status'] == 'good':
          working = True

    if rom and desc and working and not clone:
      print ('"' + rom + '", "' + desc.replace('"', '\\"') + '",')
#    romOK = False
#    dscOK = False
