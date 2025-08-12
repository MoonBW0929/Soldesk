import React, { useState } from "react";

const MoonRS3 = () => {
    const [num, set_num] = useState([50, 10, 14, 25, 74, 32]);

    num.filter((n) => n & 2 === 0);
    
    const num_re = num.map((v, i) => {
        return <marquee behavior="alternate">{v}</marquee>
    });

    return <div>{num_re}</div>;
};

export default MoonRS3;
