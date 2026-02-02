import React, { useEffect, useState } from 'react';

const Teams = () => {
  const [teams, setTeams] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;

  useEffect(() => {
    console.log('Fetching from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setTeams(results);
        console.log('Fetched teams:', results);
      })
      .catch(err => console.error('Error fetching teams:', err));
  }, [endpoint]);

  const allKeys = Array.from(
    teams.reduce((keys, item) => {
      Object.keys(item).forEach(k => keys.add(k));
      return keys;
    }, new Set())
  );

  return (
    <div className="container mt-4">
      <h1 className="mb-4">Teams</h1>
      <div className="card">
        <div className="card-body">
          <div className="table-responsive">
            <table className="table table-striped table-bordered">
              <thead className="table-dark">
                <tr>
                  {allKeys.length === 0 ? <th>No Data</th> : allKeys.map(key => <th key={key}>{key}</th>)}
                </tr>
              </thead>
              <tbody>
                {teams.length === 0 ? (
                  <tr><td colSpan={allKeys.length || 1} className="text-center">No teams found.</td></tr>
                ) : (
                  teams.map((team, idx) => (
                    <tr key={team.id || idx}>
                      {allKeys.map(key => <td key={key}>{String(team[key] ?? '')}</td>)}
                    </tr>
                  ))
                )}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Teams;
