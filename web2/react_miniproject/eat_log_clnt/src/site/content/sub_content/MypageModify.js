import axios from "axios";
import { useEffect, useRef, useState } from "react";
import { useDispatch } from "react-redux";
import { useNavigate, useSearchParams } from "react-router-dom";
import { set_profile } from "../../../slice/AccountSlice";
import "./sub_content.css";
import {
    contain_check,
    duplicate_check,
    empty_check,
    equal_check,
    minLen_check,
    onlyPhoto_check,
} from "../../../etc/MoonValidChecker";

let set = [];
set[0] = "abcdefghijklmnopqrstuvwxyz";
set[1] = "ABCDEFGHIJKLMNOPQRSTUVWZYZ";
set[2] = "1234567890";
set[3] = "-_.@#!";
set[4] = "abc123";
set[5] = "!@#iop";

const MypageModify = () => {
    const [content] = useSearchParams();
    const [val, set_val] = useState();
    const [re_pw, set_re_pw] = useState();
    const navigate = useNavigate();
    const input_img = useRef();
    const dispatcher = useDispatch();

    useEffect(() => {
        set_val(content.get("value"));
    }, [content]);

    const change_val = (evt) => {
        if (evt.target.name === "img") {
            set_val(evt.target.files[0]);
        } else {
            set_val(evt.target.value);
        }
    };

    const change_re_pw = (evt) => {
        set_re_pw(evt.target.value);
    }

    const valid_check = async (name, data) => {
        if (
            name === "pw" &&
            (empty_check(val) ||
                minLen_check(val, 4) ||
                equal_check(val, re_pw) ||
                contain_check(set[0], val) ||
                contain_check(set[2], val))
        ) {
            alert("비밀번호가 올바르지 않습니다");
            return false;
        }

        if(val !== data.name){

            if (name === "name" && (empty_check(val) || (await duplicate_check(val, "a_name")))) {
                alert("닉네임이 올바르지 않습니다");
                return false;
            }
        }

        if (name === "birth" && empty_check(val)) {
            alert("생일이 올바르지 않습니다");
            return false;
        }

        if (name === "img" && (empty_check(val) || onlyPhoto_check(val))) {
            alert("사진이 올바르지 않습니다");
            return false;
        }

        return true;
    };

    const update_info = (evt) => {

        axios
            .get(
                `http://195.168.9.125:4567/account.get.info?token=${sessionStorage.getItem(
                    "login_jwt"
                )}`
            )
            .then(async (res) => {
                if (res.data.result) {

                    if(await valid_check(evt.target.name, res.data)){
                    
                        if (evt.target.name === "img") {
                            const param = new FormData();
                            param.append("img", val);
                            param.append("id", res.data.id);
                            param.append("prevImg", res.data.img);
    
                            axios
                                .post(
                                    "http://195.168.9.125:4567/account.update.profile",
                                    param,
                                    {
                                        headers: {
                                            "Content-Type": "multipart/form-data",
                                        },
                                        withCredentials: true,
                                    }
                                )
                                .then((res2) => {
                                    if (res2.data.result) {
                                        sessionStorage.setItem(
                                            "login_jwt",
                                            res2.data.jwt
                                        );
                                        alert("정보 업데이트 완료");
                                        navigate("/mypage");
                                        window.location.reload();
                                    } else alert(res2.data.err);
    
                                    // dispatcher(set_profile(false));
                                });
                        } else {
                            axios
                                .get(
                                    `http://195.168.9.125:4567/account.update?id=${res.data.id}&content=${evt.target.name}&value=${val}`
                                )
                                .then((res2) => {
                                    if (res2.data.result) {
                                        sessionStorage.setItem(
                                            "login_jwt",
                                            res2.data.jwt
                                        );
                                        alert("정보 업데이트 완료");
                                        navigate("/mypage");
                                        window.location.reload();
                                    } else alert(res2.data.err);
    
                                    // dispatcher(set_profile(false));
                                });
                        }
                    }
                }
            });
    };

    if (content.get("content") === "img") {
        return (
            <table id="table_Mypage_modify" style={{ marginTop: 150 }}>
                <tr>
                    <td id="table_Mypage_modify_title">프로필 사진 변경</td>
                </tr>
                <tr>
                    <td>
                        <input
                            name="img"
                            type="file"
                            ref={input_img}
                            onChange={change_val}
                        />
                    </td>
                </tr>
                <tr>
                    <td>
                        <button name="img" onClick={update_info}>
                            변경
                        </button>
                    </td>
                </tr>
            </table>
        );
    } else if (content.get("content") === "birth") {
        return (
            <table id="table_Mypage_modify" style={{ marginTop: 465 }}>
                <tr>
                    <td id="table_Mypage_modify_title">생일 변경</td>
                </tr>
                <tr>
                    <td>변경할 생일 입력</td>
                </tr>
                <tr>
                    <td>
                        <input type="date" value={val} onChange={change_val} />
                    </td>
                </tr>
                <tr>
                    <td>
                        <button name="birth" onClick={update_info}>
                            변경
                        </button>
                    </td>
                </tr>
            </table>
        );
    } else if (content.get("content") === "pw") {
        return (
            <table id="table_Mypage_modify" style={{ marginTop: 250 }}>
                <tr>
                    <td id="table_Mypage_modify_title">비밀번호 변경</td>
                </tr>
                <tr>
                    <td>변경할 비밀번호 입력</td>
                </tr>
                <tr>
                    <td>
                        <input value={val} onChange={change_val} />
                    </td>
                </tr>
                <tr>
                    <td>변경할 비밀번호 재입력</td>
                </tr>
                <tr>
                    <td>
                        <input value={re_pw} onChange={change_re_pw} />
                    </td>
                </tr>
                <tr>
                    <td>
                        <button
                            name={content.get("content")}
                            onClick={update_info}
                        >
                            변경
                        </button>
                    </td>
                </tr>
            </table>
        );
    } else if (content.get("content") === "name") {
        return (
            <table id="table_Mypage_modify" style={{ marginTop: 360 }}>
                <tr>
                    <td id="table_Mypage_modify_title">닉네임 변경</td>
                </tr>
                <tr>
                    <td>변경할 닉네임 입력</td>
                </tr>
                <tr>
                    <td>
                        <input value={val} onChange={change_val} />
                    </td>
                </tr>
                <tr>
                    <td>
                        <button
                            name={content.get("content")}
                            onClick={update_info}
                        >
                            변경
                        </button>
                    </td>
                </tr>
            </table>
        );
    }
};

export default MypageModify;
