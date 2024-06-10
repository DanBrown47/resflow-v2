import React, { useState, useCallback } from 'react';
import axios from 'axios';
import { useDropzone } from 'react-dropzone';

const UploadForm = () => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');

  const onDrop = useCallback((acceptedFiles, rejectedFiles) => {
    if (acceptedFiles.length > 0) {
      setFile(acceptedFiles[0]);
      setError('');
    }

    if (rejectedFiles.length > 0) {
      setError('Unsupported file type. Only PDF, DOCX, and TXT files are allowed.');
      setFile(null);
    }
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: '.pdf,.docx,.txt',
    maxFiles: 1,
  });

  const handleSubmit = async (event) => {
    event.preventDefault();
    setMessage('');
    setError('');

    if (!name || !email || !file) {
      setError('All fields are required.');
      return;
    }

    const formData = new FormData();
    formData.append('name', name);
    formData.append('email', email);
    formData.append('file', file);

    try {
      const response = await axios.post('http://127.0.0.1:8000/api/resume/upload/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });

      if (response.status === 201) {
        setMessage('Resume uploaded successfully!');
        setName('');
        setEmail('');
        setFile(null);
      } else {
        setError('Failed to upload resume.');
      }
    } catch (error) {
      if (error.response && error.response.data) {
        handleBackendErrors(error.response.data);
      } else {
        setError('An unexpected error occurred while uploading the resume.');
      }
    }
  };

  const handleBackendErrors = (data) => {
    if (data.name) {
      setError(`Name Error: ${data.name.join(', ')}`);
    } else if (data.email) {
      setError(`Email Error: ${data.email.join(', ')}`);
    } else if (data.file) {
      setError(`File Error: ${data.file.join(', ')}`);
    } else {
      setError('An error occurred while uploading the resume.');
    }
  };

  return (
    <div>
      <h1>Upload Resume</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Name:</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </div>
        <div>
          <label>Email:</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>
        <div {...getRootProps()} style={dragAndDropStyle}>
          <input {...getInputProps()} />
          {isDragActive ? 
            <p>Drop the file here ...</p> :
            <p>Drag 'n' drop a resume here, or click to select one (PDF, DOCX, TXT)</p>
          }
        </div>
        {file && <p>Selected file: {file.name}</p>}
        <button type="submit">Upload</button>
      </form>
      {message && <p style={{ color: 'green' }}>{message}</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
};

const dragAndDropStyle = {
  border: '2px dashed #cccccc',
  padding: '20px',
  textAlign: 'center',
  cursor: 'pointer'
};

export default UploadForm;