import React, { useState } from 'react'

const MoonInput = () => {

  const [txt, set_txt] = useState("");

  return (
    <div>
      <h1>MoonInput</h1>
      <input 
        // txt의 값을 input 값에 연동
        value={txt}
        // input의 값이 바뀔때마다 txt의 값을 업데이트 
        onChange={(v) => { set_txt(v.target.value) }}
      />
    </div>
  );
};

export default MoonInput;