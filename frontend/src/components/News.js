
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const News = () => {
  const [news, setNews] = useState([]);

  useEffect(() => {
    // Выполните GET-запрос к вашему эндпоинту API новостей
    axios.get('/api/news/')
      .then(response => {
        setNews(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the news!', error);
      });
  }, []);

  return (
    <div>
      <h1>News Page</h1>
      <ul>
        {news.map(item => (
          <li key={item.id}>{item.title}</li>
        ))}
      </ul>
      <p>Привет</p>
    </div>
  );
};

export default News;