import axios from "axios";
import { useEffect, useState } from "react";
import io from "socket.io-client";

const socket = io("http://localhost:5678");

const ConsumptionTable = () => {
    const [consump_info, set_consump_info] = useState({
        detail: "",
        price: "",
        date: "",
    });
    const [consump_list, set_consump_list] = useState([]);
    const [page, set_page] = useState({
        c_page: 1,
        m_page: 0,
    });

    const consumption_get = () => {
        // axios
        //     .get(`http://195.168.9.125:4567/consumption.get.all`)
        //     .then((res) => {
        //         if (res.data.execute_ok) socket.emit("get_table", res);
        //     });

        axios
            .get(`http://195.168.9.125:4567/consumption.get?page=${page.c_page}`)
            .then((res) => {
                if (res.data.execute_ok) socket.emit("get_table", res);
            });
    };

    const consumption_reg = () => {
        axios
            .get(
                `http://195.168.9.125:4567/consumption.reg?detail=${consump_info.detail}&price=${consump_info.price}&date=${consump_info.date}`
            )
            .then((res) => {
                if (res.data.execute_ok) {
                    set_consump_info({ detail: "", price: "", date: "" });
                    socket.emit("reg_table", consump_info);
                }
            });
    };

    useEffect(() => {
        socket.on("get_table_rev", (rev_msg) => {
            set_page({...page, m_page: rev_msg.data.month_cnt});
            set_consump_list(rev_msg.data.consumption);
        });

        socket.on("reg_table_rev", (rev_msg) => {

            consumption_get();
        });

        consumption_get();

        return () => {
            socket.off("get_table_rev");
            socket.off("reg_table_rev");
        };
    }, []);

    const list = consump_list.map((v, i) => {
        let date = `${v.date.substring(0, 8)}-${v.date.substring(
            9,
            11
        )}:${v.date.substring(11, 13)}`;

        return (
            <tr align="center">
                <td>{v.detail}</td>
                <td>{v.price}</td>
                <td>{date}</td>
            </tr>
        );
    });

    const change_page = (evt) => {
        if(evt.target.className === "btn_prev"){
            alert("ok");
            if(page.c_page > 1) set_page({...page, c_page: page.c_page-1});
            consumption_get();
        }
        else if(evt.target.className === "btn_next") {
            alert("ok");
            if(page.c_page < page.m_page) set_page({...page, c_page: page.c_page+1});
            consumption_get();
        }
    }

    return (
        <>
            <table border={1}>
                <tr align="center">
                    <th colSpan={2}>소비 내역 등록</th>
                </tr>
                <tr align="center">
                    <td>소비 내용</td>
                    <td>
                        <input
                            value={consump_info.detail}
                            onChange={(evt) => {
                                set_consump_info({
                                    ...consump_info,
                                    detail: evt.target.value,
                                });
                            }}
                        />
                    </td>
                </tr>
                <tr align="center">
                    <td>소비 금액</td>
                    <td>
                        <input
                            value={consump_info.price}
                            onChange={(evt) => {
                                set_consump_info({
                                    ...consump_info,
                                    price: evt.target.value,
                                });
                            }}
                        />
                    </td>
                </tr>
                <tr align="center">
                    <td>소비 날짜</td>
                    <td>
                        <input
                            type="datetime-local"
                            value={consump_info.date}
                            onChange={(evt) => {
                                set_consump_info({
                                    ...consump_info,
                                    date: evt.target.value,
                                });
                            }}
                        />
                    </td>
                </tr>
                <tr align="center">
                    <td colSpan={2}>
                        <button onClick={consumption_reg}>등록</button>
                    </td>
                </tr>
            </table>
            <hr />

            <button className="btn_prev" onClick={change_page}>prev</button>
            <span> {page.c_page}/{page.m_page} </span>
            <button className="btn_next" onClick={change_page}>next</button>
            <br />
            <br />

            <table border={1}>
                <tr>
                    <th>소비 내용</th>
                    <th>가격</th>
                    <th>날짜</th>
                </tr>
                {list}
            </table>
        </>
    );
};

export default ConsumptionTable;
