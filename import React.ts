import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
    const [devices, setDevices] = useState([]);

    useEffect(() => {
        axios.get('/api/devices')
            .then(res => setDevices(res.data))
            .catch(console.error);
    }, []);

    return (
        <div>
            <h1>MikroTik Devices</h1>
            <ul>
                {devices.map(device => (
                    <li key={device.id}>
                        {device.name} - {device.ip}
                        <button onClick={() => rebootDevice(device.id)}>Reboot</button>
                    </li>
                ))}
            </ul>
        </div>
    );
}

function rebootDevice(deviceId) {
    axios.post(`/api/device/${deviceId}/reboot`)
        .then(console.log)
        .catch(console.error);
}

export default App;