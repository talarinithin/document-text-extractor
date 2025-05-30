import React, { useState } from 'react';

export default function UploadComponent() {
  const [file, setFile] = useState(null);
  const [text, setText] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [uploaded, setUploaded] = useState(false);

  // Just select and "upload" the file locally (no server call here)
  const handleFileChange = e => {
    setFile(e.target.files[0]);
    setText('');
    setError('');
    setUploaded(false);
  };

  // Simulate upload by confirming file is selected
  const handleUpload = () => {
    if (!file) {
      setError('Please select a file first');
      return;
    }
    setError('');
    setUploaded(true);
    setText('');
  };

  // Extract text from already uploaded file by sending to backend
  const handleExtract = async () => {
    if (!uploaded || !file) {
      setError('Please upload a file before extracting');
      return;
    }

    setLoading(true);
    setError('');
    setText('');

    const formData = new FormData();
    formData.append('file', file);

    try {
      const res = await fetch('http://localhost:5000/extract-text', {
        method: 'POST',
        body: formData,
      });
      const data = await res.json();
      if (res.ok) {
        setText(data.text || 'No text found');
      } else {
        setError(data.error || 'Error extracting text');
      }
    } catch (err) {
      setError('Network error');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Upload Document</h2>

      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload} style={{ marginLeft: 10 }}>
        Upload File
      </button>

      <button 
        onClick={handleExtract} 
        disabled={!uploaded || loading} 
        style={{ marginLeft: 10 }}
      >
        {loading ? 'Extracting...' : 'Extract Text'}
      </button>

      {error && <p style={{ color: 'red', marginTop: 10 }}>{error}</p>}

      {text && (
        <div style={{ whiteSpace: 'pre-wrap', marginTop: 20, border: '1px solid #ccc', padding: 10 }}>
          <h3>Extracted Text:</h3>
          <p>{text}</p>
        </div>
      )}
    </div>
  );
}
