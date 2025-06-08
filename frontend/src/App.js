import { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import Header from './components/Header';
import Search from './components/Search';
import ImageCard from './components/ImageCard';

const UNPLASH_KEY = process.env.REACT_APP_UNSPLASH_KEY;

const App = () => {
  const [word, setWord] = useState('');
  const [images, setImages] = useState([]);

  console.log(images);

  const handleSearchSubmit = (e) => {
    e.preventDefault(); // Correct spelling
    console.log(word);
    fetch(
      `https://api.unsplash.com/photos/random/?query=${word}&client_id=${UNPLASH_KEY}`,
    )
      .then((res) => res.json())
      .then((data) => {
        setImages([data, ...images]);
        console.log(images);
      })
      .catch((err) => {
        console.log(err);
      });
    setWord('');
  };

  return (
    <div>
      <Header title="Images Gallery 3" />
      <Search word={word} setWord={setWord} handleSubmit={handleSearchSubmit} />
      <ImageCard />
    </div>
  );
};

export default App;
