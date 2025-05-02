from pywinauto import Application

app = Application(backend='uia')
app.connect(path="keymanager.exe", timeout=4)
# app.connect(title='ATNSOFT Key Manager v1.11', best_match='ATNSOFT Key Manager v1.11', timeout=4)

elements = [item for w in app.windows() for item in w.descendants() if item.friendly_class_name() == 'TreeItem']

found_items = []


def parse_str(string: str):
    return string.split(' - ')[1].split(', T')[0][1:-1:]


def get_parents(element, found: list):
    if parse_str(str(element.parent())) != '':
        found.insert(0, parse_str(str(element.parent())))
        get_parents(element.parent(), found)

def expand_item(find_string):
    for index, element in enumerate(elements):
        if index == 0:
            pass
        try:
            element.expand()
        except:
            pass
        expand_subitem(element, find_string)
        try:
            element.collapse()
        except:
            pass
    for index, element in enumerate(elements):
        collapse_item()


def expand_subitem(subitem, find_string):
    global found_items
    if len(subitem.sub_elements()) > 0:
        for index, element in enumerate(subitem.sub_elements()):
            try:
                element.expand()
                expand_subitem(element, find_string)
            except:
                if find_string.lower() in str(element).lower():
                    found_item = []
                    found_item.append(parse_str(str(element)))
                    get_parents(element, found_item)
                    found_items.append(found_item)
            try:
                element.collapse()
            except:
                pass
    else:
        pass


def collapse_item():
    for index, element in enumerate(elements):
        try:
            element.collapse()
        except:
            pass
        collapse_subitem(element)

def collapse_subitem(subitem):
    global found_items
    if len(subitem.sub_elements()) > 0:
        for index, element in enumerate(subitem.sub_elements()):
            try:
                element.expand()
                collapse_subitem(element)
            except:
                pass
    else:
        pass