import { useEffect, useRef } from "react";
import { useDispatch } from "react-redux";
import { Link } from "react-router-dom";
import { set_size } from "../../slice/AccountSlice";
import LoginForm from "../content/sub_content/LoginForm";

const SideBar = () => {
    const tableRef = useRef(null);
    const dispatcher = useDispatch();

    useEffect(() => {
        sideBar_resize();

        window.addEventListener("resize", sideBar_resize);

        return () => {
            window.removeEventListener("resize", sideBar_resize);
        };
    }, []);

    const sideBar_resize = () => {
        if (tableRef.current) {
            const rect = tableRef.current.getBoundingClientRect();
    
            dispatcher(
                set_size({
                    left: rect.left + window.scrollX + rect.width,
                    top: rect.top + window.scrollY,
                })
            );
        }
    };

    return (
        <div>
            <table id="table_SideBar" ref={tableRef}>
                <tr>
                    <td id="td_loginform">
                        <LoginForm />
                    </td>
                </tr>
                <tr>
                    <td class="td_content">
                        <Link class="Link_SideBar" to="/">
                            홈
                        </Link>
                    </td>
                </tr>
                <tr>
                    <td class="td_content">
                        <Link class="Link_SideBar" to="/inquiry">
                            식사 기록 조회
                        </Link>
                    </td>
                </tr>
                <tr>
                    <td class="td_content">
                        <Link class="Link_SideBar" to="/search">
                            주변 가게 찾기
                        </Link>
                    </td>
                </tr>
                <tr>
                    <td class="td_content">
                        <Link class="Link_SideBar" to="/recom">
                            메뉴 추천 받기
                        </Link>
                    </td>
                </tr>
                <tr></tr>
            </table>
        </div>
    );
};

export default SideBar;
