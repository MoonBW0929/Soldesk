import { useState } from "react";
import "../style/menu_style.css";
import ConsumpManageReg from "./ConsumpManageReg";
import ConsumpManageView from "./ConsumpManageView";
import ConsumpManageDel from "./ConsumpManageDel";

const ConsumpManage = () => {
    const [sub_menu, set_sub_menu] = useState();

    const show_reg_consump = () => {
        set_sub_menu(<ConsumpManageReg />);
    };
    const show_del_consump = () => {
        set_sub_menu(<ConsumpManageDel />);
    };
    const show_view_consump = () => {
        set_sub_menu(<ConsumpManageView />);
    };
    const show_modify_consump = () => {
        set_sub_menu("");
    };

    return (
        <table id="table_menu" align="center">
            <tr>
                <td id="td_title" colSpan={4}>
                    소비 관리 사이트
                </td>
            </tr>
            <tr>
                <table id="table_choice" align="center">
                    <tr>
                        <td>
                            <span onClick={show_reg_consump}>
                                소비 내역 등록
                            </span>
                        </td>
                        <td>
                            <span onClick={show_del_consump}>
                                소비 내역 삭제
                            </span>
                        </td>
                        <td>
                            <span onClick={show_view_consump}>
                                소비 내역 조회
                            </span>
                        </td>
                        <td>
                            <span onClick={show_modify_consump}>
                                소비 내역 수정
                            </span>
                        </td>
                    </tr>
                </table>
            </tr>
            <tr>{sub_menu}</tr>
        </table>
    );
};

export default ConsumpManage;
