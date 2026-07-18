from pathlib import Path
iteminfo = {

}
def detect(items):
    for item in items:
        if item[0] != '.':
            if '.' in item:
                info = Path(item)
                iteminfo[info.suffix] = info.stem
            else:
                iteminfo['.dir'] = item
    return iteminfo