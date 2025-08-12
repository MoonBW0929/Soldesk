import React from "react";
import { Link, useNavigate } from "react-router-dom";

const MoonP1 = () => {
    
    const navi = useNavigate();

    return (
        <>
            <div>MoonP1</div>
            <hr />
            <Link to="/p4.go/몽쉘/5000">go p4</Link>&nbsp;
            <Link to="/p4.go/마이쮸/500">go p4</Link>
            <hr />
            <Link to="/p5.go?name=홍길동&age=20">go p5</Link>&nbsp;
            <Link to="/p5.go?name=김길동&age=30">go p5</Link>
            <hr />
            <button 
                onDoubleClick={() => {
                    navi("/p6.go");
                    // navi(-1);
                }}
            >
                go p6
            </button>
        </>
    );
};

export default MoonP1;
