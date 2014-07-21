# class Settings: 
#     def __init__(self):
#         import os
#         x=__import__(os.environ['DJANGO_SETTINGS_MODULE'],'','',[''])
        
#         self.REGISTER=getattr(x, 'REGISTER', False)
        
        
# if not globals().has_key('settings'): 
#     settings=Settings()