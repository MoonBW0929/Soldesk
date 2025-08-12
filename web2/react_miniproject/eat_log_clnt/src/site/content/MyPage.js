import axios from "axios";
import { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { Link, Outlet, useNavigate } from "react-router-dom";
import { set_login } from "../../slice/AccountSlice";

const MyPage = () => {
    const [userInfo, set_userInfo] = useState({
        ready: false,
        id: "",
        pw: "",
        name: "",
        birth: "",
        img: "",
    });
    const dispatcher = useDispatch();
    const navigate = useNavigate();

    const get_login_info = () => {
        axios
            .get(
                `http://195.168.9.125:4567/account.get.info?token=${sessionStorage.getItem(
                    "login_jwt"
                )}`
            )
            .then((res) => {
                if (res.data.result) {
                    set_userInfo({
                        ready: true,
                        id: res.data.id,
                        pw: res.data.pw,
                        name: res.data.name,
                        birth: res.data.birth,
                        img: res.data.img,
                    });
                }
            });
    };

    useEffect(() => {
        get_login_info();
    }, []);

    const delete_account = () => {
        axios
            .get(
                `http://195.168.9.125:4567/account.get.info?token=${sessionStorage.getItem(
                    "login_jwt"
                )}`
            )
            .then((res) => {
                if (res.data.result) {
                    axios
                        .get(
                            `http://195.168.9.125:4567/account.delete?id=${res.data.id}&table=${res.data.table}`
                        )
                        .then((res) => {
                            if (res.data.result) {
                                sessionStorage.removeItem("login_jwt");
                                dispatcher(set_login(false));
                                alert("회원 탈퇴 완료");
                                navigate("/");
                            } else alert(res.data.err);
                        });
                }
            });
    };

    if (userInfo.ready) {
        return (
            <table id="table_Mypage_main">
                <tr>
                    <td width={"60%"}>
                        <table
                            id="table_Mypage_info"
                            class="table_basicApp"
                            align="right"
                        >
                            <tr>
                                <th class="th_basicApp_title">
                                    <span>회원 정보 확인</span>
                                </th>
                            </tr>
                            <tr>
                                <td class="td_basicApp_list">
                                    <table
                                        id="table_Mypage_list"
                                        align="center"
                                    >
                                        <tr>
                                            <td class="td_Mypage_list_name">
                                                아이디
                                            </td>
                                            <td class="td_Mypage_list_content">
                                                {userInfo.id}
                                            </td>
                                            <td></td>
                                        </tr>
                                        <tr>
                                            <td class="td_Mypage_list_name">
                                                프로필 사진
                                            </td>
                                            <td>
                                                <img
                                                    src={`http://195.168.9.125:4567/eatLog.get.img?img=${userInfo.img}`}
                                                    alt=""
                                                    width={100}
                                                    height={100}
                                                />
                                            </td>
                                            <td class="td_Mypage_list_mdf">
                                                <Link
                                                    class="Link_Mypage"
                                                    to={`/mypage/modify?content=img&value=${""}`}
                                                >
                                                    {">"}
                                                </Link>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td class="td_Mypage_list_name">
                                                비밀번호
                                            </td>
                                            <td class="td_Mypage_list_content">
                                                {userInfo.pw}
                                            </td>
                                            <td class="td_Mypage_list_mdf">
                                                <Link
                                                    class="Link_Mypage"
                                                    to={`/mypage/modify?content=pw&value=${userInfo.pw}`}
                                                >
                                                    {">"}
                                                </Link>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td class="td_Mypage_list_name">
                                                닉네임
                                            </td>
                                            <td class="td_Mypage_list_content">
                                                {userInfo.name}
                                            </td>
                                            <td class="td_Mypage_list_mdf">
                                                <Link
                                                    class="Link_Mypage"
                                                    to={`/mypage/modify?content=name&value=${userInfo.name}`}
                                                >
                                                    {">"}
                                                </Link>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td class="td_Mypage_list_name">
                                                생일
                                            </td>
                                            <td class="td_Mypage_list_content">
                                                {userInfo.birth.substring(
                                                    0,
                                                    4
                                                ) +
                                                    "." +
                                                    userInfo.birth.substring(
                                                        4,
                                                        6
                                                    ) +
                                                    "." +
                                                    userInfo.birth.substring(
                                                        6,
                                                        8
                                                    )}
                                            </td>
                                            <td class="td_Mypage_list_mdf">
                                                <Link
                                                    class="Link_Mypage"
                                                    to={`/mypage/modify?content=birth&value=${""}`}
                                                >
                                                    {">"}
                                                </Link>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td class="td_Mypage_list_name">
                                                탈퇴
                                            </td>
                                            <td id="td_Mypage_btn" colSpan={2}>
                                                <button
                                                    onClick={delete_account}
                                                >
                                                    회원 탈퇴
                                                </button>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td style={{ verticalAlign: "top" }}>
                        <Outlet />
                    </td>
                </tr>
            </table>
        );
    }
};

export default MyPage;
