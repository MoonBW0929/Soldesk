import React, { useState } from "react";
import axios from "axios";

const MoonAjax1 = () => {
    const [weather, set_weather] = useState({
        sts: "",
        temp: 0,
        humi: 0,
    });

    // 동기식
    const weather_update = () => {
        axios
            .get(
                "https://api.openweathermap.org/data/2.5/weather?q=seoul&appid=baff8f3c6cbc28a4024e336599de28c4&lang=kr"
            )
            .then((res) => {
                let data = res.data;

                set_weather({
                    sts: data.weather[0].description,
                    temp: data.main.temp,
                    humi: data.main.humidity,
                });
            });
    };

    return (
        <>
            <h2>날씨 : {weather.sts}</h2>
            <h2>기온 : {weather.temp}</h2>
            <h2>습도 : {weather.humi}</h2>
            <button onClick={weather_update}>날씨 업데이트</button>
        </>
    );
};

export default MoonAjax1;
