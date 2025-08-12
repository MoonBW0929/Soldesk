import React from "react";
import { useDispatch } from "react-redux";
import { bigger, smaller } from "../MoonSizeSlice";

const MoonBtn = () => {

    const dispatch = useDispatch();

    return (
        <>
            <button
                onClick={() => {
                    dispatch(bigger());
                }}
            >
                크게
            </button>

            <button
                onClick={() => {
                    dispatch(smaller());
                }}
            >
                작게
            </button>
        </>
    );
};

export default MoonBtn;
