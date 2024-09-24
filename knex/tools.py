from langchain_core.runnables import RunnableLambda


def __object_validation(obj):
    """
    This function is made to be transformed into a LangChain Runnable.
    It checks if data extracted by the LLM is valid (eg not "Unknown")
    """

    if obj is None: return None

    # List of unwanted values given by the LLM
    forbidden = ['', 'unknown', 'unspecified', 'na', 'none']

    # If the object is just a value, check it directly
    if isinstance(obj, int) or isinstance(obj, str) or isinstance(obj, float) or isinstance(obj, bool):
        if str(obj).lower() in forbidden: return None
        else: return obj

    # If the object is an iterable, check each element
    if isinstance(obj, list) or isinstance(obj, tuple):
        new_list = []
        for elt in obj: new_list.append(__object_validation(elt))
        if isinstance(obj, list): return new_list
        elif isinstance(obj, tuple): return tuple(new_list)

    # If the object is already a dictionary, loop through all the values
    if isinstance(obj, dict):
        for key, value in obj.items():
            obj[key] = __object_validation(value)
        return obj

    # If the object is a class instance, loop through all the values
    for key, value in obj.__dict__.items():
        new_value = __object_validation(value)
        setattr(obj, key, new_value)
    return obj


# Make a Langchain element
obj_validation = RunnableLambda(__object_validation)