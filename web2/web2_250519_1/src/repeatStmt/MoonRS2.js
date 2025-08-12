import React, { useState } from "react";

const MoonRS2 = () => {
    const [val, set_val] = useState(["a", "b", "c", "d"]);

    // const val_var = val.map((v, i) => {
    //     return (
    //         <div>{v}</div>
    //     )
    // });

    const val_var = val.map((v, i) => <div>{v}</div>);

    return <div>{val_var}</div>;
};

export default MoonRS2;
