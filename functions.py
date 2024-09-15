def find_index(list,key,value):
    id=-1
    for index,val in enumerate(list):
        if(val[key]==value):
            id=index
            break
    return id


def find_by_name(list,nome):
    for item in list:
        if item['nome']==nome:
            return item
    return ''