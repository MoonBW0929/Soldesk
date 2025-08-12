import React, { useEffect, useState } from "react";
import io from "socket.io-client";

const MoonWSClnt = () => {
    const [socket, set_socket] = useState();

    useEffect(() => {
        set_socket(io("http://localhost:5678"));

        return () => {};
    }, []);

    return (
        <div
            onClick={() => {
                socket.emit("test", "ㅋ");
            }}
        >
            MoonWSClnt
        </div>
    );
};

export default MoonWSClnt;
