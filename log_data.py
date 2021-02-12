Log_Data_Dict = [
    {'log_name': 'TerminalServices-LocalSessionManager',
     'log_file': '%SystemRoot%\System32\Winevt\Logs\Microsoft-Windows-TerminalServices-LocalSessionManager%4Operational.evtx',
     'events': [
         {'event_id': '21',
          'event_name': 'logon',
          'event_data': [
              'User', 'SessionID', 'Address',
          ]
          },
         {'event_id': '22',
          'event_name': 'shell start',
          'event_data': [
              'User', 'SessionID', 'Address',
          ]
          },
         {'event_id': '23',
          'event_name': 'logoff',
          'event_data': [
              'User', 'SessionID',
          ]
          },
         {'event_id': '24',
          'event_name': 'disconnected',
          'event_data': [
              'User', 'SessionID', 'Address',
          ]
          },
         {'event_id': '25',
          'event_name': 'reconnection',
          'event_data': [
              'User', 'SessionID', 'Address',
          ]
          },
     ]
     },
]