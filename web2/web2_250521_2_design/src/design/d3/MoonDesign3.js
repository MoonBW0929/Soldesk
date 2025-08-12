import React, { useEffect } from "react";
import d3 from "./d3.module.css";

const MoonDesign3 = () => {
    
    useEffect(() => {
        const h = 180;
        const w = 80;

        // alert("키 : "+h+"cm, 몸무게 : "+w+"kg");
        alert(`키 : ${h}cm, 몸무게 : ${w}kg`);
    
    }, [])
    

    return (
        <>
            <div className={`${d3.c} ${d3.bgc} ${d3.f}`}>MD3dddd</div>
        </>
    );
};

export default MoonDesign3;
