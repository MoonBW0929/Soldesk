import React, { useState } from "react";

const MoonTest = () => {
    
    const [size, set_size] = useState(30)
    
    const change_size = (evt) => {
        if(evt.target.name === "big") set_size(size+1)
        else if(evt.target.name === "small") {
            if(size > 1) set_size(size-1)
        }
    }

    return (
        <>
            <h1 style={{fontSize: size}}>zzz</h1>
            <button name="big" onClick={change_size}>크게</button>
            <button name="small" onClick={change_size}>작게</button>
        </>
    );
};

export default MoonTest;
