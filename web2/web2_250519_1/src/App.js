import './App.css';
import MoonCss from './css/moonCss';
import MoonCss2 from './css/moonCss2';
import MoonCss3 from './css/moonCss3';
import MoonInput from './input/moonInput';
import MoonProps from './props/MoonProps';
import MoonProps2 from './props/MoonProps2';
import MoonProps3 from './props/MoonProps3';
import MoonRS from './repeatStmt/MoonRS';
import MoonRS2 from './repeatStmt/MoonRS2';
import MoonRS3 from './repeatStmt/MoonRS3';
import MoonRS4 from './repeatStmt/MoonRS4';

function App() {
  return (
    <>
      <MoonInput/>
      <hr />
      <MoonProps name="moon" age="20" />
      <hr />
      <MoonProps2 name="moon2" age="25" />
      <hr />
      <MoonProps3>test</MoonProps3>
      <hr />
      <MoonCss bgc="white" c="black" w={200} />
      <MoonCss bgc="yellow" c="blue" w={300} />
      <hr />
      <MoonCss2 />
      <hr />
      <MoonCss3 />
      <hr />
      <MoonRS />
      <hr />
      <MoonRS2 />
      <hr />
      <MoonRS3 />
      <hr />
      <MoonRS4 />
    </>
  );
}

export default App;
