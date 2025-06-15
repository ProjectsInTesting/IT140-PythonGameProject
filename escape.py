rooms = {
    'Break Room': {'North': 'QA Lab', 'South': 'Manufacturing Line', 'East': 'Parts Inventory', 'West': 'AI Core'},
    'QA Lab': {'South': 'Break Room', 'East': 'Server Room'},
    'Server Room': {'West': 'QA Lab'},
    'Manufacturing Line': {'North': 'Break Room', 'East': 'Tool Crib'},
    'Tool Crib': {'West': 'Manufacturing Line'},
    'Parts Inventory': {'West': 'Break Room', 'North': 'Maintenance Bay'},
    'Maintenance Bay': {'South': 'Parts Inventory'},
    'AI Core': {'East': 'Break Room'}
}
