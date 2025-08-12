import React, { useState } from "react";

const MoonCss2 = () => {
    const [size, set_size] = useState({ w: 300, h: 300 });

    function change_size_w(v) {
        set_size({ ...size, w: v.target.value * 1 });
    }

    function change_size_h(v) {
        set_size({ ...size, h: v.target.value * 1 });
    }

    return (
        <table border={1} style={{ width: size.w, height: size.h }}>
            <tr>
                <td>
                    <input value={size.w} onChange={change_size_w} />
                </td>
            </tr>
            <tr>
                <td>
                    <input value={size.h} onChange={change_size_h} />
                </td>
            </tr>
        </table>
    );
};

export default MoonCss2;
