import React from 'react';

const ButtonComponent = ({ onClick, loading }) => {
  return (
    <div className="text-center mt-4">
      <button className='btn btn-primary' onClick={onClick} disabled={loading}>
        {loading ? 'Loading...' : 'New Image'}
      </button>
    </div>
  );
};

export default ButtonComponent;
