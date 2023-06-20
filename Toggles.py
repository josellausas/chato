from llaulib.chato import Notapi

DEV_MODE = True # TODO: Pull this from .env file
kPROD = 'Production'
kDEV = 'Develop'

cached_response = False
cached_timestamp = False

def get_toggle_status(toggle):
    return toggle.properties.Status.status.name

def get_toggle_name(toggle):
    return toggle.properties.Name.title[0].plain_text
    
def is_enabled(toggle):
    status = get_toggle_status(toggle)
    if DEV_MODE and status == kDEV:
        return True
    elif status == kPROD:
        return True
    return False
    

class Toggle:
    name = ''
    status = ''
    enabled = False
    isDev = False
    def __init__(self, notionObj) -> None:
        self.name = get_toggle_name(notionObj)
        self.status = get_toggle_status(notionObj)
        self.isDev = get_toggle_status(notionObj) == kDEV
        self.enabled = is_enabled(notionObj)
        
        
def get_dict_of_toggles(toggle_array):
    d = {}
    for t in toggle_array:
        d[t.name] = t
    return d

def get_and_print_toggles():
    tool = Notapi.NotionTool()
    toggles = []
    
    for t in tool.get_toggles():
        toggles.append(Toggle(t))
    
    toggle_dict = get_dict_of_toggles(toggles)
    for t_name,v in toggle_dict.items():
        state = 'OFF'
        if v.enabled:
            state = 'ON'
        print(f"{t_name}: {state} {v.status}")
    
if __name__ == "__main__":
    get_and_print_toggles()