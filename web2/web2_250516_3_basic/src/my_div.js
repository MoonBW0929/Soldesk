import { useState } from "react";

const Mydiv = () => {

    const [color, set_color] = useState({bc : "white", c : "black"});
    const [color_h1, set_h1_color] = useState({bc : "white", c : "black"});

    const change_color = (e) => {
        let c = {bc : e.target.value, c : color.c}
        set_color(c);
    }

    const change_color2 = (e) => {
        let c = {bc : color.bc, c : e.target.value}
        set_color(c);
    }

    const change_h1_color = () => {
        set_h1_color(color);
    }

    return (
        <div>
            <h1 style={{backgroundColor:color_h1.bc, color:color_h1.c}}>Color</h1>
            배경색 : <input value={color.bc} onChange={change_color}/>
            <br />
            글자색 : <input value={color.c} onChange={change_color2}/>
            <br />
            <button onClick={change_h1_color}>change color</button>
        </div>
    );
};

export default Mydiv;