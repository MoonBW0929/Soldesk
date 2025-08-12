import { useState } from "react";

const MoonRS4 = () => {
    const [snack, set_snack] = useState([
        { name: "칙촉", price: 4000 },
        { name: "포카칩", price: 2300 },
        { name: "마이쮸", price: 800 },
        { name: "양파링", price: 2000 },
    ]);

    snack.sort((s1, s2) => {
        if(s1.name > s2.name) return 1;
        else return -1;
    });

    const snacks = snack.map((v, i) => {
        return(
            <tr>
                <td>{v.name}</td>
                <td>{v.price}</td>
            </tr>
        )
    });

    return <table border={1}>{snacks}</table>;
};

export default MoonRS4;
