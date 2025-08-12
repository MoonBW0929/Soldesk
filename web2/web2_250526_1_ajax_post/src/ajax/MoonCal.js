import React, { useState } from 'react'
import axios from "axios"

const MoonCal = () => {
  
    const [cal_val, set_cal_val] = useState({
        x: "",
        y: "",
    })
    const [cal_result, set_cal_result] = useState({
        plus: "",
        minus: "",
        multiple: "",
        devision: "",
    });

    const calculation = () => {
        // axios
        //     .get(
        //         `http://195.168.9.125:4567/calculation?x=${cal_val.x}&y=${cal_val.y}`
        //     )
        //     .then((res) => {
        //         set_cal_result({
        //             plus: res.data.plus,
        //             minus: res.data.minus,
        //             multiple: res.data.multiple,
        //             devision: res.data.devision,
        //         });
        //     });

        const param = new FormData();
        param.append("x", cal_val.x);
        param.append("y", cal_val.y);

        axios
            .post(
                "http://195.168.9.125:4567/calculation.post", param,
                {
                    withCredentials: true,
                }
            )
            .then((res) => {
                set_cal_result({
                    plus: res.data.plus,
                    minus: res.data.minus,
                    multiple: res.data.multiple,
                    devision: res.data.devision,
                });
            });
    };

    const change_val = (evt) => {
        
        if(evt.target.className === "input_x"){
            set_cal_val({
                ...cal_val, x: evt.target.value
            })
        }
        else if(evt.target.className === "input_y"){
            set_cal_val({
                ...cal_val, y: evt.target.value
            })
        }
    }

    return (
    <>
        X : <input className="input_x" value={cal_val.x} onChange={change_val}/>
        <br />
        Y : <input className="input_y" value={cal_val.y} onChange={change_val}/>
        <br />
        <button onClick={calculation}>calculation</button>
        <hr />
        <span>{cal_result.plus} / {cal_result.minus} / {cal_result.multiple} / {cal_result.devision}</span>
    </>
  )
}

export default MoonCal;