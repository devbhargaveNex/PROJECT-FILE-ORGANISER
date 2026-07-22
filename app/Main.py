import scan as s
import detect as d
import move as m


root = './unsorted'
items = s.scan(root)

fileinfo = d.detect(items)
for ext , name in fileinfo.items():
    print(f'filename is {name} and it is a {ext}')

result = m.move(fileinfo)
print(result)