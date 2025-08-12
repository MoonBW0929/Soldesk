import React from "react";
import axios from "axios";

const MoonP3 = () => {
    const show_menu = () => {
        axios
            .get(
                `http://195.168.9.125:4567/menu.get?token=${sessionStorage.getItem(
                    "my_jwt"
                )}`
            )
            .then((res) => {
                if (res.data.result) alert(JSON.stringify(res.data));
                else alert(res.data.comment);
            });
    };

    return (
        <>
            <div>MoonP3</div>
            <button onClick={show_menu}>확인</button>
        </>
    );
};

export default MoonP3;
