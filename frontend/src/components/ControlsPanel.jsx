import { api, getErrorMessage } from "../api";

function ControlsPanel({ setLogs, setDiagnostics }) {
  const train = async () => {
    try {
      const res = await api.post("/train", {
        model_type: "mlp",
        target_column: "target",
        params: {
          epochs: 20,
          hidden_units: 32,
          learning_rate: 0.001
        }
      });

      setLogs(res.data.logs);
      setDiagnostics(res.data.diagnostics);
    } catch (error) {
      alert(getErrorMessage(error));
    }
  };

  return (
    <div className="card">
      <h3 className="section-title">2. Train model</h3>
      <p className="section-subtitle">
        Uses an MLP with default hyperparameters on the uploaded dataset.
      </p>
      <div className="card-center">
        <button className="btn-primary" onClick={train}>
          Train Model
        </button>
      </div>
    </div>
  );
}

export default ControlsPanel;
