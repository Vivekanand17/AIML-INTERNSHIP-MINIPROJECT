import React, { useState } from "react";
import UploadForm from "./components/UploadForm";
import ControlsPanel from "./components/ControlsPanel";
import LossChart from "./components/LossChart";
import Diagnostics from "./components/Diagnostics";

function App() {
  const [logs, setLogs] = useState(null);
  const [diagnostics, setDiagnostics] = useState(null);

  return (
    <div className="app-root">
      <div className="app-shell">
        <header className="app-header">
          <h1 className="app-title">ML Training Diagnostics</h1>
          <p className="app-subtitle">
            Upload a dataset, trigger training, and explore loss curves and
            diagnostics in a focused dark interface.
          </p>
        </header>

        <main className="app-layout">
          <section className="left-column">
            <UploadForm />
            <ControlsPanel setLogs={setLogs} setDiagnostics={setDiagnostics} />
          </section>

          <section className="right-column">
            <div className="card chart-card">
              <h3 className="section-title">Training vs validation loss</h3>
              <p className="section-subtitle">
                Track how the model learns across epochs.
              </p>
              <div className="chart-container">
                {logs ? (
                  <LossChart logs={logs} />
                ) : (
                  <p className="section-subtitle">
                    Run a training job to see the loss curve.
                  </p>
                )}
              </div>
            </div>

            {diagnostics && <Diagnostics diagnostics={diagnostics} />}
          </section>
        </main>
      </div>
    </div>
  );
}

export default App;
