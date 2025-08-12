import React, { useState } from "react";
import axios from "axios";

const MoonJWT = () => {
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

    const show_menu = () => {
        axios
            .get(
                `http://195.168.9.125:4567/menu.get?token=${sessionStorage.getItem("my_jwt")}`
            )
            .then((res) => {
                if(res.data.result) alert(JSON.stringify(res.data));
                else alert(res.data.comment);
            });
    };

    const del_menu = () => {
        sessionStorage.removeItem("my_jwt");
    }

    const update_menu = () => {
        axios
            .get(
                `http://195.168.9.125:4567/menu.update?token=${sessionStorage.getItem("my_jwt")}`
            )
            .then((res) => {
                if(res.data.result) sessionStorage.setItem("my_jwt", res.data.jwt);
                else alert(res.data.comment);
            });
    }

    return (
        <>
            메뉴명 :{" "}
            <input name="name" value={menu.name} onChange={change_menu} />
            <br />
            가격 :{" "}
            <input name="price" value={menu.price} onChange={change_menu} />
            <hr />
            <button onClick={reg_menu}>등록</button>
            <button onClick={show_menu}>확인</button>
            <button onClick={del_menu}>삭제</button>
            <button onClick={update_menu}>갱신</button>
        </>
    );
};

export default MoonJWT;
