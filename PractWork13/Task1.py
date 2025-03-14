import xml.etree.ElementTree as ET

tree = ET.parse('example.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)

for elem in root.iter('tagname'): 
    elem.text = 'новое значение'

new_elem = ET.Element('new_tag')
new_elem.text = 'новое значение'
root.append(new_elem)

tree.write('modified_example.xml')
