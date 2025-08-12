import React, { useEffect } from "react";

const MoonSocketClnt = () => {
    useEffect(() => {
        window.io.connect("http://localhost:5678");

        return () => {};
    }, []);

    return <div>MoonSocketClnt</div>;
};

export default MoonSocketClnt;
