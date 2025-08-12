import React, { useRef, useState } from "react";
import axios from "axios";

const ConsumpManageReg = () => {

    const input_img = useRef();

    const [consump_info, set_consump_info] = useState({
        detail: "",
        price: "",
        date: "",
        img: "",
    });

    const change_consump_info = (evt) => {
        set_consump_info({
            ...consump_info,
            [evt.target.name]: evt.target.value,
        });
    };

    const reg_consumption = () => {

        const param = new FormData();
        param.append("detail", consump_info.detail);
        param.append("price", consump_info.price);
        param.append("date", consump_info.date);
        param.append("img", consump_info.img);

        axios
            .post("http://195.168.9.125:4567/consumption.reg", param, {
                headers: { "Content-Type": "multipart/form-data" },
                withCredentials: true,
            })
            .then((res) => {
                if(res.data.result) alert("등록 성공");
                else alert("등록 실패");
            });
    }

    return (
        <table id="table_reg_menu" align="center">
            <tr>
                <th colSpan={2}>소비 내역 등록</th>
            </tr>
            <tr>
                <td>구매처</td>
                <td>
                    <input
                        name="detail"
                        value={consump_info.detail}
                        onChange={change_consump_info}
                    />
                </td>
            </tr>
            <tr>
                <td>금액</td>
                <td>
                    <input
                        name="price"
                        value={consump_info.price}
                        onChange={change_consump_info}
                    />
                </td>
            </tr>
            <tr>
                <td>날짜</td>
                <td>
                    <input
                        name="date"
                        type="datetime-local"
                        value={consump_info.date}
                        onChange={change_consump_info}
                    />
                </td>
            </tr>
            <tr>
                <td>사진</td>
                <td>
                    <input
                        name="img"
                        type="file"
                        ref={input_img}
                        onChange={(evt) => {
                            set_consump_info({ ...consump_info, img: evt.target.files[0] });
                        }}
                    />
                </td>
            </tr>
            <tr>
                <td colSpan={2}>
                    <button onClick={reg_consumption}>등록</button>
                </td>
            </tr>
        </table>
    );
};

export default ConsumpManageReg;
