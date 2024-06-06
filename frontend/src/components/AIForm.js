
import React, { useState } from 'react';
import axios from 'axios';

const AIForm = () => {
  const [text, setText] = useState('');
  const [result, setResult] = useState('');
  const [framework, setFramework] = useState('tensorflow');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const url = framework === 'tensorflow'
      ? 'http://localhost:8001/predict_tf'
      : 'http://localhost:8002/predict_pt';
    try {
      const response = await axios.post(url, { text });
      setResult(response.data.prediction);
    } catch (error) {
      console.error('Error making prediction:', error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Введите текст"
        />
        <div>
          <label>
            <input
              type="radio"
              value="tensorflow"
              checked={framework === 'tensorflow'}
              onChange={() => setFramework('tensorflow')}
            />
            TensorFlow
          </label>
          <label>
            <input
              type="radio"
              value="pytorch"
              checked={framework === 'pytorch'}
              onChange={() => setFramework('pytorch')}
            />
            PyTorch
          </label>
        </div>
        <button type="submit">Отправить</button>
      </form>
      {result && <p>Результат: {result}</p>}
    </div>
  );
};

export default AIForm;

