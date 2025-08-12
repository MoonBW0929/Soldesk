import { useEffect, useRef, useState } from "react";

const KakaoMapSearch = () => {
    const mapRef = useRef(null);
    const [keyword, setKeyword] = useState("");
    const [places, setPlaces] = useState([]);

    // useEffect(() => {
    //     const mapContainer = mapRef.current;
    //     const mapOption = {
    //         center: new window.kakao.maps.LatLng(37.566826, 126.9786567),
    //         level: 3,
    //     };

    //     const map = new window.kakao.maps.Map(mapContainer, mapOption);
    //     const ps = new window.kakao.maps.services.Places();
    //     const infowindow = new window.kakao.maps.InfoWindow({ zIndex: 1 });

    //     const displayPlaces = (placesData) => {
    //         setPlaces(placesData);
    //         const bounds = new window.kakao.maps.LatLngBounds();
    //         placesData.forEach((place) => {
    //             const position = new window.kakao.maps.LatLng(place.y, place.x);
    //             const marker = new window.kakao.maps.Marker({ map, position });
    //             bounds.extend(position);

    //             window.kakao.maps.event.addListener(marker, "mouseover", () => {
    //                 infowindow.setContent(
    //                     `<div style="padding:5px;">${place.place_name}</div>`
    //                 );
    //                 infowindow.open(map, marker);
    //             });
    //             window.kakao.maps.event.addListener(marker, "mouseout", () => {
    //                 infowindow.close();
    //             });
    //         });
    //         map.setBounds(bounds);
    //     };

    //     if (keyword.trim() !== "") {
    //         ps.keywordSearch(keyword, (data, status) => {
    //             if (status === window.kakao.maps.services.Status.OK) {
    //                 displayPlaces(data);
    //             } else {
    //                 alert("검색 결과가 없습니다.");
    //             }
    //         });
    //     }
    // }, [keyword]);

    useEffect(() => {
        mapSearch();
    }, []);

    const mapSearch = () => {
        const mapContainer = mapRef.current;
        const mapOption = {
            center: new window.kakao.maps.LatLng(37.566826, 126.9786567),
            level: 3,
        };

        const map = new window.kakao.maps.Map(mapContainer, mapOption);
        const ps = new window.kakao.maps.services.Places();
        const infowindow = new window.kakao.maps.InfoWindow({ zIndex: 1 });

        const displayPlaces = (placesData) => {
            setPlaces(placesData);
            const bounds = new window.kakao.maps.LatLngBounds();
            placesData.forEach((place) => {
                const position = new window.kakao.maps.LatLng(place.y, place.x);
                const marker = new window.kakao.maps.Marker({ map, position });
                bounds.extend(position);

                window.kakao.maps.event.addListener(marker, "mouseover", () => {
                    infowindow.setContent(
                        `<div style="padding:5px;">${place.place_name}</div>`
                    );
                    infowindow.open(map, marker);
                });
                window.kakao.maps.event.addListener(marker, "mouseout", () => {
                    infowindow.close();
                });
            });
            map.setBounds(bounds);
        };

        if (keyword.trim() !== "") {
            ps.keywordSearch(keyword, (data, status) => {
                if (status === window.kakao.maps.services.Status.OK) {
                    displayPlaces(data);
                } else {
                    alert("검색 결과가 없습니다.");
                }
            });
        }
    };

    const handleSearch = () => {
        if (!keyword.trim()) {
            alert("키워드를 입력해주세요!");
            return;
        } else {
            mapSearch();
        }
        // setKeyword(keyword);
    };

    return (
        <table id="table_KaKaoMapSearch" border={1}>
            <tr>
                <td height={50}>
                    <input
                        type="text"
                        placeholder="장소 검색"
                        onChange={(e) => setKeyword(e.target.value)}
                        value={keyword}
                    />
                    <button onClick={handleSearch}>검색</button>
                </td>
                <td rowSpan={2} style={{ width: 200 }}>
                    <ul>
                        {places.map((place, index) => (
                            <li key={index}>
                                <strong>{place.place_name}</strong>
                                <p>
                                    {place.road_address_name ||
                                        place.address_name}
                                </p>
                                <p>{place.phone}</p>
                            </li>
                        ))}
                    </ul>
                </td>
            </tr>
            <tr>
                <td>
                    <div
                        id="map"
                        ref={mapRef}
                        style={{ width: "100%", height: "100%" }}
                    ></div>
                </td>
            </tr>
        </table>
    );
};

export default KakaoMapSearch;
