
init -2 python:
    # splits a item_array in even chunks of blok_size
    def split_list_in_blocks(list, blok_size):
        for i in range(0, len(list), blok_size):
            yield list[i:i + blok_size]


    # finds an item in a list, where search(item) == True
    # search as lambda could be a lambda ==> x: x.name == 'searchname'
    def find_in_list(search, list):
        for item in list:
            if search(item):
                return item
        return None
    
    # finds all qualifying items in list and returns them as a smaller list.
    def find_items_in_list(search, list):
        items = []
        for item in list:
            if search(item):
                items.append(item)
        if items != []:
            return items
        else:
            return None

    def simple_list_format(list_to_format, what_to_format, string = "", ignore = "", attrib = ""): # Returns a simple list for use in generic menus. Extensive use in the Biotech Actions.
        tuple_list = []                                                    # NOTE: Needed a generic list setup, this seems to cover most usecases I came across.
        for what_to_format in list_to_format:
            if what_to_format is not ignore:
                
                if attrib is not "":
                    tuple_string = str(string) + str(vars(what_to_format)[attrib]) # e.g attrib = "name" for SerumTrait.name to be displayed
                    tuple_list.append([tuple_string, what_to_format])
                
                else:
                    tuple_string = str(string) + str(what_to_format)
                    tuple_list.append([tuple_string, what_to_format])
            else:
                tuple_string = str(what_to_format)
                tuple_list.append([tuple_string, what_to_format])
        return tuple_list
