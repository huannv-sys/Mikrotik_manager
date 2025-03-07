from flask import Flask, jsonify
from librouteros import connect
from easysnmp import Session
from models import db, Device

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pass@localhost/mikrotik_db'
db.init_app(app)

# Kết nối MikroTik qua API
def mikrotik_api(host, user, password):
    try:
        conn = connect(username=user, password=password, host=host)
        return conn
    except Exception as e:
        return {'error': str(e)}

# Kết nối MikroTik qua SNMPv3
def mikrotik_snmp(host, user, auth_pass, enc_pass):
    try:
        session = Session(
            hostname=host,
            security_level='auth_with_privacy',
            security_username=user,
            auth_password=auth_pass,
            auth_protocol='SHA',
            priv_password=enc_pass,
            priv_protocol='AES'
        )
        return session
    except Exception as e:
        return {'error': str(e)}

# Lấy thông tin hệ thống qua SNMPv3
def get_system_info(host, user, auth_pass, enc_pass):
    session = mikrotik_snmp(host, user, auth_pass, enc_pass)
    if 'error' in session:
        return session
    sys_name = session.get('1.3.6.1.2.1.1.5.0').value
    sys_uptime = session.get('1.3.6.1.2.1.1.3.0').value
    return {'sys_name': sys_name, 'sys_uptime': sys_uptime}

# Điều khiển thiết bị qua API
def reboot_device(host, user, password):
    conn = mikrotik_api(host, user, password)
    if 'error' in conn:
        return conn
    conn(cmd='/system/reboot')
    return {'status': 'success'}

# API Endpoint
@app.route('/api/device/<int:device_id>/info')
def device_info(device_id):
    device = Device.query.get(device_id)
    info = get_system_info(device.ip, device.snmp_user, device.snmp_auth_pass, device.snmp_enc_pass)
    return jsonify(info)

@app.route('/api/device/<int:device_id>/reboot')
def device_reboot(device_id):
    device = Device.query.get(device_id)
    result = reboot_device(device.ip, device.api_user, device.api_password)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0')