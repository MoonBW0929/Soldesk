import "./App.css";
import MoonEvent1 from "./event/MoonEvent1";
import MoonKeyEvent from "./event/MoonKeyEvent";
import MoonMouseEvent from "./event/MoonMouseEvent";
import MoonPopupMenu from "./event/MoonPopupMenu";
import MoonPopupMenu2 from "./event/MoonPopupMenu2";
import MoonResizeEvent from "./event/MoonResizeEvent";
import MoonHook1 from "./hook/MoonHook1";
import MoonHook2 from "./hook/MoonHook2";
import MoonHook3 from "./hook/MoonHook3";
import MoonHook4 from "./hook/MoonHook4";
import MoonSocketClnt from "./socket/MoonSocketClnt";

function App() {
    return (
    <>
      <MoonKeyEvent />
      <hr />
      <MoonEvent1 />
      <hr />
      <MoonPopupMenu />
      <hr />
      <MoonMouseEvent />
      <hr />
      <MoonHook1 />
      <hr />
      <MoonHook2 />
      <hr />
      <MoonHook3 />
      <hr />
      <MoonResizeEvent />
      <hr />
      <MoonPopupMenu2 />
      <MoonHook4 />
      <hr />
      <MoonSocketClnt />
    </>
    );
}

export default App;
