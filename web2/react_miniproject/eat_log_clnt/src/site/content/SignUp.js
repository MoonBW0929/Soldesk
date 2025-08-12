import axios from "axios";
import { useRef, useState } from "react";
import { useNavigate, useSearchParams } from "react-router-dom";
import {
    available_check,
    contain_check,
    duplicate_check,
    empty_check,
    equal_check,
    minLen_check,
    onlyPhoto_check,
} from "../../etc/MoonValidChecker";
import "./content.css";
import { useSelector } from "react-redux";

let set = [];
set[0] = "abcdefghijklmnopqrstuvwxyz";
set[1] = "ABCDEFGHIJKLMNOPQRSTUVWZYZ";
set[2] = "1234567890";
set[3] = "-_.@#!";
set[4] = "abc123";
set[5] = "!@#iop";

const SignUp = () => {
    const navigate = useNavigate();
    const input_img = useRef();
    const [pos] = useSearchParams();
    const subscriber = useSelector((store) => store.AccountSlice);
    const [ac_info, set_ac_info] = useState({
        id: "",
        pw: "",
        re_pw: "",
        name: "",
        birth: "",
        img: "",
    });

    const pos_style = {
        position: "absolute",
        left: pos.get("left") + "px",
        top: pos.get("top") + "px",
    };

    const valid_check = async () => {
        if (
            empty_check(ac_info.id) ||
            minLen_check(ac_info.id, 4) ||
            available_check(ac_info.id) ||
            (await duplicate_check(ac_info.id, "a_id"))
        ) {
            alert("아이디가 올바르지 않습니다");
            return false;
        }

        if (
            empty_check(ac_info.pw) ||
            minLen_check(ac_info.pw, 4) ||
            equal_check(
                ac_info.pw,
                ac_info.re_pw ||
                    contain_check(set[0], ac_info.pw) ||
                    contain_check(set[2], ac_info.pw)
            )
        ) {
            alert("비밀번호가 올바르지 않습니다");
            return false;
        }

        if (
            empty_check(ac_info.name) ||
            (await duplicate_check(ac_info.name, "a_name"))
        ) {
            alert("닉네임이 올바르지 않습니다");
            return false;
        }

        if (empty_check(ac_info.birth)) {
            alert("생일이 올바르지 않습니다");
            return false;
        }

        if (empty_check(ac_info.img) || onlyPhoto_check(ac_info.img)) {
            alert("사진이 올바르지 않습니다");
            return false;
        }

        return true;
    };

    const reg_account = async () => {
        if (await valid_check()) {
            const param = new FormData();
            param.append("id", ac_info.id);
            param.append("pw", ac_info.pw);
            param.append("name", ac_info.name);
            param.append("birth", ac_info.birth);
            param.append("img", ac_info.img);

            axios
                .post("http://195.168.9.125:4567/account.reg", param, {
                    headers: { "Content-Type": "multipart/form-data" },
                    withCredentials: true,
                })
                .then((res) => {
                    if (res.data.result) {
                        alert("등록 성공");
                        navigate(
                            `/login?left=${subscriber.left}&top=${subscriber.top}`
                        );
                    } else alert("등록 실패");
                });
        }
    };

    const change_ac_info = (evt) => {
        if (evt.target.name === "img") {
            set_ac_info({
                ...ac_info,
                img: evt.target.files[0],
            });
        } else {
            set_ac_info({
                ...ac_info,
                [evt.target.name]: evt.target.value,
            });
        }
    };

    return (
        <table id="table_signup" style={pos_style}>
            <tr>
                <th id="th_signup_title" colSpan={2}>
                    회원 가입
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
                <td>비밀번호 재입력</td>
                <td>
                    <input
                        name="re_pw"
                        type="password"
                        value={ac_info.re_pw}
                        onChange={change_ac_info}
                    />
                </td>
            </tr>
            <tr>
                <td>닉네임</td>
                <td>
                    <input
                        name="name"
                        value={ac_info.name}
                        onChange={change_ac_info}
                    />
                </td>
            </tr>
            <tr>
                <td>생일</td>
                <td>
                    <input
                        name="birth"
                        type="date"
                        value={ac_info.birth}
                        onChange={change_ac_info}
                    />
                </td>
            </tr>
            <tr>
                <td>프로필 사진</td>
                <td>
                    <input
                        name="img"
                        type="file"
                        ref={input_img}
                        onChange={change_ac_info}
                    />
                </td>
            </tr>
            <tr>
                <td colSpan={2}>
                    <button onClick={reg_account}>Sign up</button>
                </td>
            </tr>
        </table>
    );
};

export default SignUp;
