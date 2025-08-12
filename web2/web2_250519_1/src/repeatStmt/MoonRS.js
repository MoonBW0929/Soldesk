import React from "react";

const MoonRS = () => {
    const exe = () => {
        let arr = [456, 586, 22, 348, 51];

        arr.map((v, i) => {
            alert(i + " / " + v);
        });
    };

    return <button onClick={exe}>button</button>;
};

export default MoonRS;
