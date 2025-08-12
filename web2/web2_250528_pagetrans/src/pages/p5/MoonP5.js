import React from "react";
import { useSearchParams } from "react-router-dom";

const MoonP5 = () => {

    const [student, set_student] = useSearchParams();

    return (
        <>
            <div>MoonP5</div>
            <div>{student.get("name")} / {student.get("age")}</div>
        </>
    );
};

export default MoonP5;
