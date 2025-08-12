import React, { useState } from "react";

const SnackTable = () => {
    const [snack, set_snack] = useState({ name: "", price: "" });
    const [snacks, set_snacks] = useState([]);

    const change_snack_name = (v) => {
        set_snack({ ...snack, name: v.target.value });
    };
    const change_snack_price = (v) => {
        set_snack({ ...snack, price: v.target.value });
    };

    const add_snack = () => {
        set_snacks(snacks.concat(snack));
        set_snack({ name: "", price: "" });
    };

    const del_snack = (name) => {
        set_snacks(snacks.filter((snack) => snack.name !== name));
    };

    const snack_table = snacks.map((v, i) => {
        return (
            <tr className="tr_snack" onClick={() => del_snack(v.name)}>
                <td>{v.name}</td>
                <td>{v.price}</td>
            </tr>
        );
    });

    return (
        <>
            이름 : <input value={snack.name} onChange={change_snack_name} />
            <br />
            가격 : <input value={snack.price} onChange={change_snack_price} />
            <br />
            <button onClick={add_snack}>추가</button>
            <hr />
            <table border={1}>
                <tr>
                    <th>이름</th>
                    <th>가격</th>
                </tr>
                {snack_table}
            </table>
        </>
    );
};

export default SnackTable;
