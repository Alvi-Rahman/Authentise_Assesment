import React from 'react';
import { Spinner } from 'react-bootstrap';

const ImageComponent = ({ imageUrl, loading }) => {
  return (
    <div className="text-center my-5">
      <div style={{ height: '300px' }}>
        {loading ? (
          <Spinner animation="border" role="status">
            <span className="sr-only">Loading...</span>
          </Spinner>
        ) : (
          <img src={imageUrl} alt="Dog" className="img-fluid rounded my-4" style={{ height: '100%' }} />
        )}
      </div>
    </div>
  );
};

export default ImageComponent;
