import axios from "axios";
import { useState } from "react";
import { useDispatch } from "react-redux";
import { useNavigate, useSearchParams } from "react-router-dom";
import { set_login } from "../../slice/AccountSlice";
import "./content.css";

const Login = () => {
    const [pos] = useSearchParams();
    const navigate = useNavigate();
    const dispatcher = useDispatch();
    const [ac_info, set_ac_info] = useState({
        id: "",
        pw: "",
    });

    const pos_style = {
        position: "absolute",
        left: pos.get("left") + "px",
        top: pos.get("top") + "px",
    };

    const change_ac_info = (evt) => {
        set_ac_info({ ...ac_info, [evt.target.name]: evt.target.value });
    };

    const login_account = () => {
        axios
            .get(
                `http://195.168.9.125:4567/account.login?id=${ac_info.id}&pw=${ac_info.pw}`
            )
            .then((res) => {
                if (res.data.result) {
                    alert("로그인 성공");
                    sessionStorage.setItem("login_jwt", res.data.jwt);
                    navigate("/");

                    axios
                        .get(
                            `http://195.168.9.125:4567/account.get.info?token=${sessionStorage.getItem(
                                "login_jwt"
                            )}`
                        )
                        .then((res) => {
                            if (res.data.result) {
                                dispatcher(set_login(true));
                            } else alert(res.data.err);
                        });
                } else alert(res.data.err);
            });
    };

    return (
        <table id="table_login" style={pos_style}>
            <tr>
                <th id="th_login_title" colSpan={2}>
                    로그인
                </th>
            </tr>
            <tr>
                <td>아이디</td>
                <td>
                    <input
                        name="id"
                        value={ac_info.id}
                        onChange={change_ac_info}
                    />
                </td>
            </tr>
            <tr>
                <td>비밀번호</td>
                <td>
                    <input
                        name="pw"
                        type="password"
                        value={ac_info.pw}
                        onChange={change_ac_info}
                    />
                </td>
            </tr>
            <tr>
                <td colSpan={2}>
                    <button onClick={login_account}>Login</button>
                </td>
            </tr>
        </table>
    );
};

export default Login;
