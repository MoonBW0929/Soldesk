import React from 'react'
import { useSelector } from 'react-redux'

const MoonH1 = () => {

    const size = useSelector((store) => store.MSizeSlice)

  return (
    <h1 style={{fontSize: size.fontSize}}>zzz</h1>
  )
}

export default MoonH1