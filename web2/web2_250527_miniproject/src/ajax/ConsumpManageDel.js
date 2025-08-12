import React, { useEffect, useState } from "react";
import axios from "axios";

const ConsumpManageDel = () => {
    const [page, set_page] = useState({
        c_page: 1,
        m_page: 0,
    });

    const [consump_list, set_consump_list] = useState([]);

    const get_month_cnt = () => {
        axios
            .get(`http://195.168.9.125:4567/consumption.month.cnt.get`)
            .then((res) => {
                if (res.data.result) {
                    set_page({ ...page, m_page: res.data.month_cnt });
                }
            });
    };

    const get_consumption = () => {
        axios
            .get(
                `http://195.168.9.125:4567/consumption.get?page=${page.c_page}`
            )
            .then((res) => {
                if (res.data.result) {
                    set_consump_list(res.data.consumption);
                }
            });
    };

    const change_page = (evt) => {
        if (evt.target.name === "prev") {
            if (page.c_page > 1) {
                let new_page = page.c_page - 1;
                set_page({ ...page, c_page: new_page });
            }
        } else if (evt.target.name === "next") {
            if (page.c_page < page.m_page) {
                let new_page = page.c_page + 1;
                set_page({ ...page, c_page: new_page });
            }
        }
    };

    const del_consumption = (evt) => {
        axios
            .get(
                `http://195.168.9.125:4567/consumption.del?no=${evt.target.name}`
            )
            .then((res) => {
                if (res.data.result) {
                    alert("삭제 성공");
                    get_consumption();
                }
                else alert("삭제 실패");
            });
    }

    useEffect(() => {
        get_month_cnt();

        get_consumption();

        return () => {};
    }, []);

    useEffect(() => {
        get_consumption();

        return () => {};
    }, [page.c_page]);

    const set_table = consump_list.map((v, i) => {
        let date = `${v.date.substring(0, 8)}-${v.date.substring(
            9,
            11
        )}:${v.date.substring(11, 13)}`;

        return (
            <tr>
                <td>
                    <table
                        style={{
                            width: 500,
                            height: 80,
                            border: "2px black solid",
                            padding: "0 0 0 0",
                            borderSpacing: 0,
                            marginTop: 10,
                            borderRadius: 20,
                            textAlign: "center",
                            fontWeight: "bold",
                        }}
                    >
                        <tr>
                            <td
                                width={100}
                                height={100}
                                rowSpan={2}
                                style={{
                                    borderRight: "2px black solid",
                                }}
                            >
                                <img
                                    style={{ width: "80%", height: "80%" }}
                                    src={`http://195.168.9.125:4567/consumption.get.img?img=${v.img}`}
                                    alt=""
                                />
                            </td>
                            <td
                                height={30}
                                style={{
                                    borderRight: "2px black solid",
                                    borderBottom: "2px black solid",
                                    width: 220,
                                    textAlign: "left",
                                    paddingLeft: 30,
                                }}
                            >
                                {v.detail}
                            </td>
                            <td
                                style={{
                                    borderBottom: "2px black solid",
                                }}
                            >
                                {date}
                            </td>
                        </tr>
                        <tr>
                            <td
                                style={{
                                    textAlign: "left",
                                    paddingLeft: 20,
                                    fontSize: 23,
                                }}
                            >
                                -{v.price}원
                            </td>
                            <td>
                                <button name={v.no} onClick={del_consumption}>삭제</button>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        );
    });

    return (
        <>
            <table 
                align="center"
                style={{marginTop: 10}}
            >
                <tr>
                    <td>
                        <div
                            style={{
                                display: "flex",
                                justifyContent: "space-between", // 요소들을 좌우 끝과 중앙에 배치
                                alignItems: "center", // 세로 정렬 맞춤
                                width: "100%", // 전체 너비 적용
                            }}
                        >
                            <button name="prev" onClick={change_page}>
                                prev
                            </button>
                            <span>
                                {page.c_page} / {page.m_page}
                            </span>
                            <button name="next" onClick={change_page}>
                                next
                            </button>
                        </div>
                    </td>
                </tr>
                {set_table}
            </table>
        </>
    );
};

export default ConsumpManageDel;
