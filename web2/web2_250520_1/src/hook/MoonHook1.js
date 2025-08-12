import React, { useState } from "react";

const MoonHook1 = () => {
    
    const [counter, set_counter] = useState(0)

    const btn_clicked = () => {
        set_counter(counter+1);        
    }

    return (
        <>
            <h2>{counter}</h2>
            <button onClick={btn_clicked}>button</button>
        </>
    );
};

export default MoonHook1;
