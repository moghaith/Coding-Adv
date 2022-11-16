import React ,{useEffect, useState} from 'react';
import './App.css';
import Backdrop from '@mui/material/Backdrop';
import CircularProgress from '@mui/material/CircularProgress';
import Button from '@mui/material/Button';
function App(){
  const [post,setPost]=useState(null);
  const [open, setOpen] = React.useState(false);
  const handleClose = () => {
    setOpen(false);
  };
  const handleToggle = () => {
    setOpen(!open);
  };
  const fetching = () => {
    fetch("https://jsonplaceholder.typicode.com/posts/1")
    .then(response=>response.json())
    .then(response => {
      const{body} = response
      setPost(body)
      
    })
    .then(document.getElementById('post').innerHTML= `${post}`)
  }
  useEffect(()=>{
    fetch("https://jsonplaceholder.typicode.com/posts/1")
    .then(response=>response.json())
    .then(response => {
      const{body} = response
      console.log(body)
      setPost(body)
    }) 
  },[])

  return (
      <div className = "div1" id='post'>

      <Button onClick={handleToggle} onAnimationEnd={fetching}>Get Post</Button>
 <Backdrop
        sx={{ color: '#fff', zIndex: (theme) => theme.zIndex.drawer + 1 }}
        open={open}
        onClick={handleClose}
      >
        <CircularProgress color="inherit"/>
      </Backdrop> 
      </div>
  );
}
export default App;
