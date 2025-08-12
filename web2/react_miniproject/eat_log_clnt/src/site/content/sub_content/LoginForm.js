import axios from "axios";
import { useDispatch, useSelector } from "react-redux";
import { Link, useNavigate } from "react-router-dom";
import { set_login } from "../../../slice/AccountSlice";
import "./sub_content.css";
import { useEffect, useState } from "react";

const LoginForm = () => {
    const subscriber = useSelector((store) => store.AccountSlice);
    const dispatcher = useDispatch();
    const navigate = useNavigate();
    const [login_info, set_login_info] = useState({
        login : false,
        name : "",
        img : "",
    })

    useEffect(() => {
        get_login_info();
    
    }, [subscriber.login])
    
    const get_login_info = () => {

        axios
            .get(
                `http://195.168.9.125:4567/account.get.info?token=${sessionStorage.getItem(
                    "login_jwt"
                )}`
            )
            .then((res) => {
                if(res.data.result){
                    set_login_info({
                        login : true,
                        name : res.data.name,
                        img : res.data.img,
                    })
                }
            })
    }

    if (!subscriber.login) {
        return (
            <div id="div_loginBefore">
                <span>
                    <Link
                        class="Link_SideBar"
                        to={`/login?left=${subscriber.left}&top=${subscriber.top}`}
                    >
                        로그인
                    </Link>
                </span>
                &nbsp;&nbsp;|&nbsp;&nbsp;
                <span>
                    <Link
                        class="Link_SideBar"
                        to={`/signup?left=${subscriber.left}&top=${subscriber.top}`}
                    >
                        회원 가입
                    </Link>
                </span>
            </div>
        );
    }

    if(login_info.login){

        return (
            <div id="div_loginAfter">
                <table id="table_loginAfter" align="center">
                    <tr>
                        <td colSpan={2}>
                            <img
                                id="img_profile"
                                src={`http://195.168.9.125:4567/eatLog.get.img?img=${login_info.img}`}
                                alt=""
                            />
                        </td>
                    </tr>
                    <tr>
                        <td colSpan={2}>
                            <span id="span_loginName">{login_info.name}</span>님
                        </td>
                    </tr>
                    <tr>
                        <td id="td_mypage">
                            <span class="span_mymenu">
                                <Link class="Link_SideBar" to={"/mypage"}>마이페이지</Link>
                            </span>
                        </td>
                        <td id="td_logout">
                            <span
                                class="span_mymenu"
                                onClick={() => {
                                    set_login_info({
                                        login : false,
                                        name : "",
                                        img : "",
                                    })
                                    dispatcher(set_login(false));
                                    sessionStorage.removeItem("login_jwt");
                                    navigate("/");
                                }}
                            >
                                로그아웃
                            </span>
                        </td>
                    </tr>
                </table>
            </div>
        );
    }
};

export default LoginForm;
