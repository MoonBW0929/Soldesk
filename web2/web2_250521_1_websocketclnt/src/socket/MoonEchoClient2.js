import { useEffect, useState } from "react";
import io from "socket.io-client";

const socket = io("http://localhost:5678");

const MoonEchoClient2 = () => {
    const [msg, set_msg] = useState();

    useEffect(() => {
        socket.on("send_rev", (rev_msg) => {
            alert(rev_msg);
        });

        return () => {
            socket.off("send_rev");
        };
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

export default MoonEchoClient2;
