import React, { useState } from "react";
import { Link } from "react-router-dom";
import axios from 'axios'

const MoonP12 = () => {

    const [menu, set_menu] = useState({
        name: "",
        price: "",
    });

    const change_menu = (evt) => {
        set_menu({ ...menu, [evt.target.name]: evt.target.value });
    };

    const reg_menu = () => {
        axios
            .get(
                `http://195.168.9.125:4567/menu.reg?name=${menu.name}&price=${menu.price}`
            )
            .then((res) => {
                if (res.data.result) {
                    sessionStorage.setItem("my_jwt", res.data.jwt);
                    set_menu({ name: "", price: "" });
                }
            });
    };

    return (
        <>
            <div>MoonP2</div>
            <a href="/p3.go">Go P3</a>&nbsp;
            <Link to="/p3.go">Go P3</Link>
            <hr />
            메뉴명 :{" "}
            <input name="name" value={menu.name} onChange={change_menu} />
            <br />
            가격 :{" "}
            <input name="price" value={menu.price} onChange={change_menu} />
            <br />
            <button onClick={reg_menu}>등록</button>
        </>
    );
};

export default MoonP12;
