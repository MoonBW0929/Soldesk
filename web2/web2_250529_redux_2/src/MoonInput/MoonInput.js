import React from "react";
import { useDispatch } from "react-redux";
import { set_text } from "../MoonTxtSlice";

const MoonInput = () => {
    
    const dispatcher = useDispatch();

    return (
        <input
            onChange={(evt) => {
                dispatcher(set_text(evt.target.value));
            }}
        />
    );
};

export default MoonInput;
