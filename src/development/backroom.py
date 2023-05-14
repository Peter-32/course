import gc
def free_up_memory(locals_dict):
    """ 
    Pass locals() as locals_dict from the notebook
    """
    for var_name in [x for x in locals_dict.keys() if not x.startswith("_") and x not in ['In', 'Out', 'get_ipython', 'exit', 'quit', 'open', 'free_up_memory', 'gc']]:
        del locals_dict[var_name]
    gc.collect()