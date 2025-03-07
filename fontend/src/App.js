import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [sites, setSites] = useState([]);

  useEffect(() => {
    axios.get('/api/sites')
      .then(res => setSites(res.data))
      .catch(console.error);
  }, []);

  return (
    <div>
      <h1>MikroTik Sites</h1>
      <ul>
        {sites.map(site => (
          <li key={site.id}>{site.name}</li>
        ))}
      </ul>
    </div>
  );
}