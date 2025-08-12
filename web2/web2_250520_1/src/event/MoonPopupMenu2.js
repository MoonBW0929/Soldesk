import React, { useEffect, useState } from "react";

const MoonPopupMenu2 = () => {
    const [pos, set_pos] = useState({ top: -100, left: -100});

    let table_css = {
        position: "absolute",
        top: pos.top,
        left: pos.left,
    };

    const show_popup = (evt) => {
        // 기존의 기능 막기
        evt.preventDefault();
    };

    const mouse_clicked = (evt) => {
        if(evt.button === 2){
            
            set_pos({
                top: evt.clientY,
                left: evt.clientX,
            });
            
            setTimeout(() => {
                
                set_pos({
                    top: -100,
                    left: -100,
                });
            }, 3000);
        }
    };

    useEffect(() => {
        document.addEventListener("contextmenu", show_popup);
        document.addEventListener("mouseup", mouse_clicked);

        return () => {
            document.removeEventListener("contextmenu", show_popup);
            document.removeEventListener("mouseup", mouse_clicked);
        };
    }, []);

    return (
        <>
            <table style={table_css}>
                <tr>
                    <td>
                        <a href="https://naver.com">naver.com</a>
                    </td>
                </tr>
                <tr>
                    <td>
                        <a href="https://google.com">google.com</a>
                    </td>
                </tr>
            </table>
        </>
    );
};

export default MoonPopupMenu2;
