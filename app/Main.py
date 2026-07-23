import scan as s
import detect as d
import move as m
import operations as o


root = './unsorted'
items = s.scan(root)
fileinfo = d.detect(items)
finallist,operation = o.operate(fileinfo,items)
if operation == "move":
    fileinfo = d.detect(finallist)
    result = m.move(fileinfo)