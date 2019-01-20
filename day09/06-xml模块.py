import xml.etree.cElementTree as ET

# tree = ET.parse('xml_test.xml')
# root = tree.getroot()
# print(root, root.tag)

# 遍历xml文档
# for child in root:
#     print(child.tag, child.attrib)
#     for item in child:
#         print(item.tag, item.text)

# 只遍历某个节点
# for node in root.iter('year'):
#     print(node.tag, node.text)

# 修改
# for node in root.iter('year'):
#     new_year = int(node.text) + 1
#     node.text = str(new_year)
#     node.set('updated', 'yes')
#
# tree.write('xml_test.xml')

# 删除
# for country in root.findall('country'):
#     rank = int(country.find('rank').text)
#     if rank > 50:
#         root.remove(country)
#
# tree.write('xml_test.xml')


# 创建xml
new_xml = ET.Element('namelist')

name = ET.SubElement(new_xml, 'name', attrib={"enrolled": "yes"})
name.text = 'ksm'
age = ET.SubElement(name, 'age', attrib={"checked": "no"})
age.text = '24'
sex = ET.SubElement(name, 'sex')
sex.text = 'b'

name = ET.SubElement(new_xml, 'name', attrib={"enrolled": "no"})
name.text = 'xml'
age = ET.SubElement(name, 'age', attrib={"checked": "no"})
age.text = '22'
sex = ET.SubElement(name, 'sex')
sex.text = 'g'

et = ET.ElementTree(new_xml)
et.write('test_xml.xml', encoding='utf8', xml_declaration=True)
