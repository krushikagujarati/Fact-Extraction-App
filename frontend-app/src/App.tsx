import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

interface IFactResponse {
  question: string;
  facts: string[] | null;
  status: 'idle' | 'processing' | 'done' | 'error';
}

const App: React.FC = () => {
  //const [apiKey, setApiKey] = useState<string>('');
  const [question, setQuestion] = useState<string>('');
  const [urls, setUrls] = useState<string>('');
  const [facts, setFacts] = useState<string[] | null>(null);
  const [status, setStatus] = useState<'idle' | 'processing' | 'done' | 'error'>('idle');

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setStatus('processing');
    setFacts(null);

    const documents = urls.split('\n').filter(url => url.trim() !== '');
    const payload = { question, documents };

    try {
      await axios.post(`${process.env.REACT_APP_SERVER_URL}/submit_question_and_documents`, payload);
      fetchFacts();
    } catch (error) {
      console.error('Error submitting question and documents:', error);
      setStatus('error');
    }
  };

  const fetchFacts = async () => {
    try {
      const response = await axios.get<IFactResponse>(`${process.env.REACT_APP_SERVER_URL}/get_question_and_facts`);
      if (response.data.status === 'done') {
        setFacts(response.data.facts);
        setStatus('done');
      } else if (response.data.status === 'processing') {
        setTimeout(fetchFacts, 1000); // Poll every second
      } else {
        console.error('1Error fetching facts:', response.data);
        setStatus('error');
      }
    } catch (error) {
      console.error('Error fetching facts:', error);
      setStatus('error');
    }
  };

  return (
    <div>
      <h1>Fact Extraction from Call Logs</h1>
      <form onSubmit={handleSubmit}>
        {/* <div>
        <label>
            OpenAI API Key:
            <input type="text" value={apiKey} onChange={(e) => setApiKey(e.target.value)} required />
        </label>
        </div> */}
        <div>
          <label>
            Question:
            <input type="text" value={question} onChange={(e) => setQuestion(e.target.value)} required />
          </label>
        </div>
        <div>
          <label>
            Document URLs (one per line):
            <textarea value={urls} onChange={(e) => setUrls(e.target.value)} required />
          </label>
        </div>
        <button type="submit">Submit</button>
      </form>
      {status === 'processing' && <p>Processing...</p>}
      {status === 'done' && facts && (
        <div className='center'>
          <h2>Extracted Facts:</h2>
          <ul>
            {facts.map((fact, index) => <li key={index}>{fact}</li>)}
          </ul>
        </div>
      )}
      {status === 'error' && <p>Error processing the request. Please try again later.</p>}
    </div>
  );
}

export default App;
