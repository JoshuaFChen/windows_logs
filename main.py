import win32evtlog

# Pseudo-code for reading Windows Events
server = "localhost"
log_type = "Microsoft-Windows-TerminalServices-LocalSessionational"
log_handle = win32evtlog.OpenEventLog(server, log_type)

flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
total = win32evtlog.GetNumberOfEventLogRecords(log_handle)

print(total)

events = win32evtlog.ReadEventLog(log_handle, flags, 0)
for event in events[0:10]:
    print('Event Category:', event.EventCategory)
    print('Time Generated:', event.TimeGenerated)
    print('Source Name:', event.SourceName)
    print('Event ID:', event.EventID & 0x1FFFFFFF)
    print('Event Type:', event.EventType)
    # data = event.StringInserts
    # if data:
    #     print('Event Data:')
    #     for msg in data:
    #         print(msg)

win32evtlog.CloseEventLog(log_handle)
