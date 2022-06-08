
def get_json_clean_response(return_value: dict):
    """
        Build a json format object based on the return_value for a specific model
    @param return_value: Dictionary that need to be serialized in at json format
    @return: Json format
    """
    if isinstance(return_value, dict):
        pass
    elif return_value is None:
        return_value = {}
    elif isinstance(return_value, list):
        items = []
        for item in return_value:
            if not isinstance(item, dict):
                items.append(item.to_dictionary())
            else:
                items.append(item)
            return_value = items
    elif isinstance(return_value, object):
        try:
            return_value = return_value.to_dictionary()
        except AttributeError:
            pass
    return return_value

