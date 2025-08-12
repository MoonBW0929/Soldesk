import React, { useEffect, useRef, useState } from "react";

const MoonHook4 = () => {
    const paper = useRef();
    const [pen, set_pen] = useState();

    const canvas_css = {
        width: 400,
        height: 300,
        border: "1px solid black",
    };

    useEffect(() => {
        set_pen(paper.current.getContext("2d"));

        return () => {};
    }, []);

    return (
        <canvas
            style={canvas_css}
            ref={paper}
            onClick={(evt) => {
                pen.fillRect(
                    evt.nativeEvent.offsetX - 25,
                    evt.nativeEvent.offsetY - 25,
                    50,
                    50
                );
            }}
        />
    );
};

export default MoonHook4;
