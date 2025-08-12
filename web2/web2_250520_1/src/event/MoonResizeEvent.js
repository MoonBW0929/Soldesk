import React, { useEffect, useState } from "react";

const MoonResizeEvent = () => {
    const [size, set_size] = useState({
        w: window.innerWidth,
        h: window.innerHeight,
    });

    const update_size = (v) => {
        set_size({
            w: window.innerWidth,
            h: window.innerHeight,
        });
    };

    useEffect(() => {
        // vanilla JS에서 이벤트 연결 방법 (window의 resize시 update_size 함수를 실행하도록 연결)
        window.addEventListener("resize", update_size);

        return () => {
            // vanilla JS에서 이벤트 연결 끊기
            window.removeEventListener("resize", update_size);
        };
    }, []);

    return (
        <>
            <h2>width : {size.w}</h2>
            <h2>height : {size.h}</h2>
        </>
    );
};

export default MoonResizeEvent;
