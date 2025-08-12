import React, { useReducer } from "react";

const MoonHook2 = () => {
    function set_action(action, flag_action){
        return action + " - " + flag_action;
    }

    const [action, add_action] = useReducer(set_action, "시작");

    const change_flag = (v) => {
        if(v.target.name === "flag1") add_action("청기 올려");
        else if(v.target.name === "flag2") add_action("청기 내려");
        else if(v.target.name === "flag3") add_action("백기 올려");
        else if(v.target.name === "flag4") add_action("백기 내려");
    }

    return (
        <>
            <div>{action}</div>
            <br />
            <button name="flag1" onClick={change_flag}>청기 올려</button>
            <button name="flag2" onClick={change_flag}>청기 내려</button>
            <button name="flag3" onClick={change_flag}>백기 올려</button>
            <button name="flag4" onClick={change_flag}>백기 내려</button>
        </>
    );
};

export default MoonHook2;
