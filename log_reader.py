import win32evtlog
from log_data import Log_Data_Dict


def get_text(text, word):
    try:
        result = text.split(f'<{word}>')[1].split(f'</{word}>')[0]
    except:
        return ''
    else:
        return result


def load_log_data(log_file):
    query_handle = win32evtlog.EvtQuery(log_file, win32evtlog.EvtQueryFilePath)
    xml_list = []
    while True:
        events = win32evtlog.EvtNext(query_handle, 1)
        # if there is no record break the loop
        if len(events) == 0:
            break
        else:
            xml_content = win32evtlog.EvtRender(events[0], win32evtlog.EvtRenderEventXml)
            xml_list.append(xml_content)
    return xml_list


def parser_user_data(event, event_id, current_log):
    user_data_list = [event for event in current_log['events'] if event['event_id'] == event_id]
    user_dict = {}
    if user_data_list:
        event_data = user_data_list[0]['event_data']
        for user_data in event_data:
            user_dict.update({user_data: get_text(event, user_data)})
    return user_dict


def parser_system_data(event):
    event_id = get_text(event, 'EventID')
    time_created = event.split('<TimeCreated SystemTime=')[1].split('/>')[0].strip("'")
    computer = get_text(event, 'Computer')
    return {
        'event_id': event_id,
        'time_created': time_created,
        'computer': computer,
    }


def iterate_all_logs():
    for current_log in Log_Data_Dict:
        event_list = load_log_data(current_log['log_file'])
        print(len(event_list))
        for event in event_list:
            event_dict = {}
            system_data = parser_system_data(event)
            event_id = system_data['event_id']
            event_dict.update(system_data)
            user_data = parser_user_data(event, event_id, current_log)
            event_dict.update(user_data)
            print(event_dict)


iterate_all_logs()


