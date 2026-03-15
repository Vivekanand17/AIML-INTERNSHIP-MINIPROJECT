import { api, getErrorMessage } from "../api";

function UploadForm() {
  const upload = async (e) => {
    if (!e.target.files || !e.target.files[0]) return;

    const formData = new FormData();
    formData.append("file", e.target.files[0]);

    try {
      await api.post("/upload", formData, {
        headers: { "Content-Type": "multipart/form-data" }
      });
      alert("Dataset uploaded successfully.");
    } catch (error) {
      alert(getErrorMessage(error));
    }
  };

  return (
    <div className="card card-inline">
      <div>
        <h3 className="section-title">1. Upload dataset (CSV)</h3>
        <p className="section-subtitle">
          Choose a CSV file to analyze and train on.
        </p>
      </div>
      <label className="file-input-label">
        <span>Select file</span>
        <input type="file" accept=".csv" onChange={upload} />
      </label>
    </div>
  );
}

export default UploadForm;
