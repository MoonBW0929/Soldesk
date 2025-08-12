import React from "react";
import { useParams } from "react-router-dom";

const MoonP4 = () => {
    const snack = useParams();

    return (
        <>
            <div>MoonP4</div>
            <div>
                {snack.name} / {snack.price}
            </div>
        </>
    );
};

export default MoonP4;
