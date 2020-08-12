from xml.etree import ElementTree

tree = ElementTree.parse('students.xml')

root = tree.getroot()

print(root)
print(root.tag, root.attrib)

for a in root:
    print(a.tag, a.attrib)
    for b in a:
        print('         ', b.tag, ': ', b.text)
        for c in b:
            print('                 ', c.tag, c.text)
