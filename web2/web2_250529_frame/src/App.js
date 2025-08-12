import "./App.css";
import Gallery from "./site/gallery/gallery";
import Home from "./site/home/home";
import Notice from "./site/notice/Notice";
import SiteLayout from "./site/SiteLayout";
import { Route, Routes } from "react-router-dom";

function App() {
    return (
        <Routes>
            <Route element={<SiteLayout />}>
                <Route path="/" element={<Home />} />
                <Route path="/gallery.go" element={<Gallery />} />
                <Route path="/Notice.go" element={<Notice />} />
            </Route>
        </Routes>
    );
}

export default App;
