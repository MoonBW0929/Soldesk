import React, { useEffect, useRef, useState } from "react";
import io from "socket.io-client";

const socket = io("http://localhost:5678");

const MoonDrawClient = () => {
    const paper = useRef();
    const [draw_sts, set_draw_sts] = useState(false);
    const [draw_info, set_draw_info] = useState({
        begin_x: 0,
        begin_y: 0,
        end_x: 0,
        end_y: 0,
        color: "black",
    });

    useEffect(() => {

        socket.on("draw_info_rev", (draw_info_rev) => {

            const pen = paper.current.getContext("2d")

            pen.strokeStyle = draw_info_rev.color;
            pen.beginPath();
            pen.moveTo(draw_info_rev.begin_x, draw_info_rev.begin_y);
            pen.lineTo(draw_info_rev.end_x, draw_info_rev.end_y);
            pen.closePath();
            pen.stroke();
        });

        socket.on("draw_sts_rev", (sts) => {
            set_draw_sts(sts);
        });

        return () => {
            socket.off("draw_info_rev");
            socket.off("draw_sts_rev");
        };
    }, []);

    const draw_line = (evt) => {
        if (draw_sts) {
            set_draw_info({
                ...draw_info,
                begin_x: draw_info.end_x,
                begin_y: draw_info.end_y,
                end_x: evt.nativeEvent.offsetX,
                end_y: evt.nativeEvent.offsetY,
            });

            socket.emit("draw_info", draw_info);
        }
    };
    
    const draw_start = (evt) => {
        if (evt.button === 0) {
            socket.emit("draw_sts", true);
            set_draw_info({
                ...draw_info,
                begin_x: evt.nativeEvent.offsetX,
                begin_y: evt.nativeEvent.offsetY,
                end_x: evt.nativeEvent.offsetX,
                end_y: evt.nativeEvent.offsetY,
            });
        }
    }

    return (
        <>
            <canvas
                style={{border: "solid 2px black"}}
                width={400}
                height={300}
                ref={paper}
                onMouseDown={draw_start}
                onMouseUp={() => {
                    socket.emit("draw_sts", false);
                }}
                onMouseMove={draw_line}
            />
            <br />
            <input 
                value={draw_info.color}
                style={{color: draw_info.color}}
                onChange={(evt) => {
                    set_draw_info({...draw_info, color: evt.target.value});
                }}
            />
            <br />
        </>
    );
};

export default MoonDrawClient;
