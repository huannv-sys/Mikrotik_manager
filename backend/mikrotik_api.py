from librouteros import connect
from datetime import datetime

def get_mikrotik_data(host, user, password):
    try:
        conn = connect(username=user, password=password, host=host)
        interfaces = conn(cmd='/interface/print')
        traffic = conn(cmd='/interface/monitor-traffic', interface='ether1', duration=5)
        return {
            'timestamp': datetime.now().isoformat(),
            'traffic': traffic[0],
            'interfaces': interfaces
        }
    except Exception as e:
        return {'error': str(e)}