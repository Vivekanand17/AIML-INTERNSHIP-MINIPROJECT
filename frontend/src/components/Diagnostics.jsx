function Diagnostics({ diagnostics }) {
  return (
    <div className="card">
      <h3 className="section-title">Diagnostics</h3>
      <p className="section-subtitle">
        Automatically detected issues and training insights.
      </p>
      <pre className="diagnostics-pre">
        {JSON.stringify(diagnostics, null, 2)}
      </pre>
    </div>
  );
}

export default Diagnostics;
