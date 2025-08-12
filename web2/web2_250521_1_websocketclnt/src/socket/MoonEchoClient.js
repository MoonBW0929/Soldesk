import { useEffect, useState } from "react";
import io from "socket.io-client";

const MoonEchoClient = () => {
    const [socket, set_socket] = useState();
    const [msg, set_msg] = useState();

    useEffect(() => {
        set_socket(io.connect("http://localhost:5678"));

        return () => {};
    }, []);

    const msg_send = () => {
        socket.emit("send", msg);
        set_msg("");
    };

    const msg_change = (evt) => {
        set_msg(evt.target.value);
    };

    return (
        <>
            <input value={msg} onChange={msg_change} />
            <button onClick={msg_send}>전송</button>
        </>
    );
};

export default MoonEchoClient;
