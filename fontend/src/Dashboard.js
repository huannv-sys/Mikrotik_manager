import React, { useState, useEffect } from 'react';

function Dashboard() {
  const [data, setData] = useState([]);

  useEffect(() => {
    // Fetch data from the backend API
    fetch('/api/mikrotik/devices')
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  return (
    <div className="Dashboard">
      <h2>Device Dashboard</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Status</th>
            <th>IP Address</th>
          </tr>
        </thead>
        <tbody>
          {data.map(device => (
            <tr key={device.id}>
              <td>{device.id}</td>
              <td>{device.name}</td>
              <td>{device.status}</td>
              <td>{device.ip_address}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Dashboard;