import { useState } from "react";

const Mytable = () => {

    const show_txt = () => {
        alert("ok");
    }

    const [input_val, set_input_val] = useState("");

    const show_input_val = () => {
        alert(input_val);
    }

    const key_up = (e) => {
        set_input_val(e.target.value);
    }

    return (
        <table border="1">
            <tr>
                <td>
                    <button onClick={show_txt}>button</button>
                </td>
            </tr>
            <tr>
                <td>
                    <input value={input_val} onChange={key_up}/>
                    <button onClick={show_input_val}>button2</button>
                </td>
            </tr>
        </table>
    );
};

export default Mytable;