import "./App.css";
import { Route, Routes } from "react-router-dom";
import MoonP1 from "./pages/p1/MoonP1";
import MoonP12 from "./pages/p1_2/MoonP12";
import MoonP3 from "./pages/p3/MoonP3";
import MoonP4 from "./pages/p4/MoonP4";
import MoonP5 from "./pages/p5/MoonP5";
import MoonP6 from "./pages/p6/MoonP6";
import MoonP7 from "./pages/p7/MoonP7";
import MoonP8 from "./pages/p8/MoonP8";

function App() {
    return (
        <Routes>
            <Route index element={<MoonP1 />} />
            <Route path="/p2.go" element={<MoonP12 />} />
            <Route path="/p3.go" element={<MoonP3 />} />
            <Route path="/p4.go/:name/:price" element={<MoonP4 />} />
            <Route path="/p5.go" element={<MoonP5 />} />
            <Route path="/p6.go" element={<MoonP6 />} />
            <Route path="/p7.go" element={<MoonP7 />} />
            <Route path="*" element={<MoonP8 />} />
        </Routes>
    );
}

export default App;
