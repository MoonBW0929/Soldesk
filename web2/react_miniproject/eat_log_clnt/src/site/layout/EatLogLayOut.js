import { Outlet, useNavigate } from "react-router-dom";
import "./layout.css";
import SideBar from "./SideBar";
import { useEffect } from "react";
import axios from "axios";
import { useDispatch, useSelector } from "react-redux";
import { set_login } from "../../slice/AccountSlice";

const EatLogLayOut = () => {

    const dispatcher = useDispatch()
    const subscriber = useSelector((store) => store.AccountSlice);
    const navigate = useNavigate();

    const login_check = () => {

        axios
            .get(
                `http://195.168.9.125:4567/account.get.info?token=${sessionStorage.getItem(
                    "login_jwt"
                )}`
            )
            .then((res) => {
                if (!res.data.result) {
                    if(res.data.err !== ""){
                        alert(res.data.err);
                        dispatcher(set_login(false));
                        sessionStorage.removeItem("login_jwt");
                        navigate("/");
                    }
                } else {

                    if(!subscriber.login)
                            dispatcher(set_login(true));

                    axios
                        .get(
                            `http://195.168.9.125:4567/account.login.update?token=${sessionStorage.getItem(
                                "login_jwt"
                            )}`
                        )
                        .then((res) => {
                            if (res.data.result) {
                                sessionStorage.setItem("login_jwt", res.data.jwt);
                            }
                        });
                }
            });
    };

    useEffect(() => {
        login_check();
        document.addEventListener("click", login_check);

        return () => {
            document.removeEventListener("click", login_check);
        };
    }, []);

    return (
        <table id="table_main" border={1}>
            <tr>
                <th id="th_Maintitle" colSpan={2}>
                    Eat Log
                </th>
            </tr>
            <tr>
                <td id="td_sidebar">
                    <SideBar />
                </td>
                <td id="td_contents">
                    <Outlet />
                </td>
            </tr>
        </table>
    );
};

export default EatLogLayOut;
