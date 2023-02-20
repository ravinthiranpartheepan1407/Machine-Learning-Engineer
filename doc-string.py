# Doc Strings used to write definitions to functions
# Can be invoked with ''' ''' or help() or function.__doc__

def doct_string(a):
    ''' Test Doc String '''
    print(a)

doct_string(1)
help(doct_string)
doct_string.__doc__