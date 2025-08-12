import React, { useRef, useState } from "react";
import axios from "axios";

const MoonPhoto = () => {
    const [photo, set_photo] = useState({
        title: "",
        photo: "",
    });
    const [result, set_result] = useState({
        title: "",
    });
    const input_photo = useRef();

    const change_photo = (evt) => {
        if (evt.target.name === "photo") {
            set_photo({ ...photo, [evt.target.name]: evt.target.files[0] });
        } else {
            set_photo({ ...photo, [evt.target.name]: evt.target.value });
        }
    };

    const upload = () => {
        const param = new FormData();
        param.append("photo", photo.photo);
        param.append("title", photo.title);

        axios
            .post("http://195.168.9.125:4567/photo.upload", param, {
                headers: {"Content-Type" : "multipart/form-data"},
                withCredentials: true,
            })
            .then((res) => {
                set_result({ ...result, title: res.data.title });
                set_photo({ title: "", photo: "" });
                input_photo.current.value = "";
            });
    };

    return (
        <>
            제목 :{" "}
            <input name="title" value={photo.title} onChange={change_photo} />
            <p />
            사진 :{" "}
            <input
                name="photo"
                type="file"
                ref={input_photo}
                onChange={change_photo}
                multiple
            />
            <p />
            <button onClick={upload}>업로드</button>
            <h2>입로드된 파일 제목 : {result.title}</h2>
        </>
    );
};

export default MoonPhoto;
