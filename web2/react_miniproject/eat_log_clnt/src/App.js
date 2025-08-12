import { Route, Routes } from "react-router-dom";
import "./App.css";
import EatLogHome from "./site/content/EatLogHome";
import EatLogInquiry from "./site/content/EatLogInquiry";
import EatLogRecom from "./site/content/EatLogRecom";
import EatLogSearch from "./site/content/EatLogSearch";
import Login from "./site/content/Login";
import SignUp from "./site/content/SignUp";
import EatLogLayOut from "./site/layout/EatLogLayOut";
import MyPage from "./site/content/MyPage";
import MypageModify from "./site/content/sub_content/MypageModify";

function App() {
    return (
        <Routes>
            <Route element={<EatLogLayOut />}>
                <Route path="/" element={<EatLogHome />} />
                <Route path="/inquiry" element={<EatLogInquiry />} />
                <Route path="/recom" element={<EatLogRecom />} />
                <Route path="/search" element={<EatLogSearch />} />
                <Route path="/signup" element={<SignUp />} />
                <Route path="/login" element={<Login />} />
                {/* <Route path="/mypage" element={<MyPage />} /> */}
                <Route path="/mypage" element={<MyPage />}>
                    <Route path="/mypage/modify" element={<MypageModify />}/>
                </Route>
            </Route>
        </Routes>
    );
}

export default App;
