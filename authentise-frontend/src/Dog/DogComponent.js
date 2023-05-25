import React, { useState, useEffect } from 'react';
import axios from 'axios';
import _ from 'lodash';
import ImageComponent from './Components/Image';
import ButtonComponent from './Components/Button';

const DogComponent = () => {
  const [imageUrl, setImageUrl] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchDogImage();
  }, []);

  const fetchDogImage = async () => {
    try {
      setLoading(true);
      const response = await axios.get('https://dog.ceo/api/breeds/image/random');
      const image = _.get(response, 'data.message', '');
      setImageUrl(image);
    } catch (error) {
      console.error('Error fetching dog image:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleNewImage = () => {
    fetchDogImage();
  };

  return (
    <div className="text-center">
      <h1>Dog Image App</h1>
      <ImageComponent imageUrl={imageUrl} loading={loading} />
      <ButtonComponent onClick={handleNewImage} loading={loading} />
    </div>
  );
};

export default DogComponent;
