import React, { useRef, useState } from "react";
import axios from "axios";

const WeatherTable = () => {

    const input_img = useRef();

    const [weather, set_weather] = useState({
        sts: "",
        temp: "",
        img: "",
    });

    const [reg_result, set_reg_result] = useState({
        result: "",
        sts: "",
        temp: "",
        img: "",
    });

    const change_weather = (evt) => {
        set_weather({ ...weather, [evt.target.name]: evt.target.value });
    };

    const reg_weather = () => {
        const param = new FormData();
        param.append("sts", weather.sts);
        param.append("temp", weather.temp);
        param.append("img", weather.img);

        axios
            .post("http://195.168.9.125:4567/weather.reg", param, {
                headers: { "Content-Type": "multipart/form-data" },
                withCredentials: true,
            })
            .then((res) => {
                if (res.data.result) {
                    set_reg_result({
                        result: "성공",
                        sts: res.data.sts,
                        temp: res.data.temp,
                        img: res.data.img,
                    });
                    
                    set_weather({
                        sts: "",
                        temp: "",
                        img: "",
                    })
                    input_img.current.value = "";
                }
            });
    };

    return (
        <>
            날씨 :{" "}
            <input name="sts" value={weather.sts} onChange={change_weather} />
            <br />
            기온 :{" "}
            <input name="temp" value={weather.temp} onChange={change_weather} />
            <br />
            이미지 :{" "}
            <input
                name="img"
                type="file"
                ref={input_img}
                onChange={(evt) => {
                    set_weather({ ...weather, img: evt.target.files[0] });
                }}
            />
            <br />
            <button onClick={reg_weather}>등록</button>
            <br />
            <h2>등록 결과 : {reg_result.result}</h2>
            <h2>등록 날씨 : {reg_result.sts}</h2>
            <h2>등록 온도 : {reg_result.temp}</h2>
            <h2>등록한 파일 이름 : {reg_result.img}</h2>
            <img
                src={`http://195.168.9.125:4567/weather.get.img?img=${reg_result.img}`}
                alt=""
            />
            <br />
            <a
                href={`http://195.168.9.125:4567/weather.get.img?img=${reg_result.img}`}
            >
            등록한 파일 다운로드
            </a>
        </>
    );
};

export default WeatherTable;
