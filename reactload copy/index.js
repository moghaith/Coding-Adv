import React, {useEffect} from 'react';
import './style.css';
function index(){
    useEffect(()=> {
        fetch("https://api.openweathermap.org/data/2.5/weather?zip=&appid=368fbbe4658dc3cb8369e650cf3b80cf&units=imperial")
        .then(response=>response.json())
        .then(response => {
            const{body}=response
            console.log(body)
        })
    },[])
    return (
        <div className = "div1">
            <button>Get Weather</button>
        </div>
    );
}
