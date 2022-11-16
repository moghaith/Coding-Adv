import React ,{useEffect, useState} from 'react';
import Button from '@mui/material/Button';
import Backdrop from '@mui/material/Backdrop';
import CircularProgress from '@mui/material/CircularProgress';
import './App.css';

function App(){
  const [open, setOpen] = React.useState(false);
  const handleClose = () => {
    setOpen(false);
  };
  const handleToggle = () => {
    setOpen(!open);
  };
  const fetching = ()=>{
    handleToggle();
    fetch("https://flash-the-slow-api.herokuapp.com/delay/4000/url/https://jsonplaceholder.typicode.com/posts/1")
    .then(response=>response.json())
    .then(response => {
      const{body} = response
      console.log(body)
      document.getElementById('post').innerHTML= `${body}`
    }) 
    .then(handleClose)
  }

  return (
      <div id='post'>
<Button onClick={fetching} >Get Post</Button>
<Backdrop
        sx={{ color: '#fff', zIndex: (theme) => theme.zIndex.drawer + 1 }}
        open={open}
        onClick={handleClose}
      >
        <CircularProgress color="inherit" />
      </Backdrop>
      </div>
  );
}
export default App;
