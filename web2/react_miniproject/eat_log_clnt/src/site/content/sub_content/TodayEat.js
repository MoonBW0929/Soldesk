import React, { useEffect } from "react";
import "./sub_content.css";
import axios from "axios";

const TodayEat = () => {

    const show_todayEat = () => {

        // axios
        //     .get(
        //         `http://195.168.9.125:4567/account.get.info?token=${sessionStorage.getItem(
        //             "login_jwt"
        //         )}`
        //     )
        //     .then((res) => {
                
        //         if(res.data.result){

        //             axios
        //                 .get(
        //                     `http://195.168.9.125:4567/eatLog.get.today?table=${res.data.table}`
        //                 )
        //                 .then((res) => {

        //                 })
        //         }
        //     })
    }

    useEffect(() => {
      show_todayEat();
    
      return () => {
      }
    }, [])
    

    return (
        <table class="table_basic_app" id="table_TodayEat">
            <tr>
                <th class="th_basicApp_title">
                    <span>오늘 먹은 메뉴는?</span>
                </th>
            </tr>
            <tr>
                <td class="td_basicApp_list">
                    <div>오늘 먹은 메뉴를 추가해 보세요!</div>
                </td>
            </tr>
        </table>
    );
};

export default TodayEat;
