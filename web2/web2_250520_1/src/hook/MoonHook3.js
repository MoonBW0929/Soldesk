import { useEffect, useReducer, useState } from "react";

const MoonHook3 = () => {
    const [color, set_color] = useState("white");
    const [color2, set_color2] = useReducer(confirm_color2, "black");

    let input_css1 = {
        backgroundColor: "red",
        color: color,
    };

    let input_css2 = {
        backgroundColor: "yellow",
        color: color2,
    };

    const change_color = (v) => {
        set_color(v.target.value);
    };
    const change_color2 = (v) => {
        set_color2(v.target.value);
    };

    function confirm_color2(color2, new_color) {
        return new_color;
    }

    useEffect(() => {
        alert("z");

        return () => {
            alert("g");
        };
    }, []);

    return (
        <>
            <input value={color} style={input_css1} onChange={change_color} />
            <br />
            <input value={color2} style={input_css2} onChange={change_color2} />
        </>
    );
};

export default MoonHook3;
