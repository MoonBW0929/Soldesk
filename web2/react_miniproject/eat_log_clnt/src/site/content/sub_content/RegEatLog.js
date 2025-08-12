import { useRef, useState } from "react";
import "./sub_content.css";
import axios from "axios";
import KakaoMapSearch from "./KakaoMapSearch";

const RegEatLog = () => {
    const input_img = useRef();
    
    const [eatLog, set_eatLog] = useState({
        store: "",
        addr: "",
        menu: "",
        price: "",
        date: "",
        img: "",
    });

    const [isPopupOpen, setIsPopupOpen] = useState(false);
    const [tempAddr, setTempAddr] = useState("");

    const openPopup = () => setIsPopupOpen(true);
    const closePopup = () => setIsPopupOpen(false);

    const saveAddr = () => {
        set_eatLog(prev => ({ ...prev, addr: tempAddr }));
        closePopup();
    };

    const Reg_eatLog = () => {
        axios
            .get(`http://195.168.9.125:4567/account.get.info?token=${sessionStorage.getItem("login_jwt")}`)
            .then((res) => {
                if (res.data.result) {
                    const param = new FormData();
                    param.append("img");

                    axios.post("http://195.168.9.125:4567/eatLog.reg", param, {
                        headers: { "Content-Type": "multipart/form-data" },
                        withCredentials: true,
                    })
                    .then((res) => {
                        if (res.data.result) {
                            alert("등록 성공");
                        } else alert("등록 실패");
                    });
                }
            });
    };

    return (
        <div>
            <table className="table_basic_app" id="table_RegEatLog">
                <tr>
                    <th className="th_basicApp_title">
                        <span>식사 등록</span>
                    </th>
                </tr>
                <tr>
                    <td id="td_RegEatLog" className="td_basicApp_list">
                        <div>
                            <button id="btn_findAddr" onClick={openPopup}>주소 찾기</button>
                            <input id="input_RegEatLog_addr" className="input_RegEatLog" value={eatLog.addr} readOnly placeholder="가게 주소"/>
                        </div>
                        <div>
                            <input className="input_RegEatLog" placeholder="가게 이름"/>
                        </div>
                        <div>
                            <input className="input_RegEatLog" placeholder="메뉴 이름"/>
                        </div>
                        <div>
                            <input className="input_RegEatLog" placeholder="메뉴 가격"/>
                        </div>
                        <div id="div_RegEatLog_date">
                            <input type="date"/>
                        </div>
                        <div id="div_RegEatLog_file">
                            <input type="file" ref={input_img}/>
                        </div>
                        <button id="btn_reg_eatLog" onClick={Reg_eatLog}>등록</button>
                    </td>
                </tr>
            </table>

            {isPopupOpen && (
                <div className="popup-overlay">
                    <div className="popup-content">
                        <h3>주소 찾기</h3>
                        <KakaoMapSearch />
                        {/* <input type="text" value={tempAddr} onChange={(e) => setTempAddr(e.target.value)} placeholder="주소 입력"/>
                        <button onClick={saveAddr}>확인</button>
                        <button onClick={closePopup}>취소</button> */}
                    </div>
                </div>
            )}
        </div>
    );
};

export default RegEatLog;