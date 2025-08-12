import axios from "axios";
import { useState } from "react";

const MoonAjax2 = () => {

    const [book_name, set_book_name] = useState("");
    const [books, set_books] = useState([]);

    const search_book = () => {

        axios.get(
            `https://dapi.kakao.com/v3/search/book?query=${book_name}`,
            {headers: {"Authorization": "KakaoAK c1f71dc8cc391306ea455cf2e1513ed3"}}
        )
        .then((res) => {
            set_books(res.data.documents);
        })

        set_book_name("");
    }

    const book_list = books.map((v, i) => {
        return (
            <tr>
                <td>
                    <img src={v.thumbnail} alt="none img"/>
                </td>
                <td>{v.title}</td>
                <td>{v.price}</td>
            </tr>
        )
    });

    return (
        <>
            <input
                value={book_name}
                onChange={(evt) => {
                    set_book_name(evt.target.value);
                }}
            />
            <button onClick={search_book}>검색</button>
            <table border={1}>
                <tr>
                    <th>사진</th>
                    <th>이름</th>
                    <th>가격</th>
                </tr>
                {book_list}
            </table>
        </>
    );
};

export default MoonAjax2;
