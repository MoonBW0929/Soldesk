import React from 'react'
import { useSelector } from 'react-redux'

const MoonH1 = () => {

    const subscriber = useSelector((store) => store.MTxtSlice);

  return (
    <h1>{subscriber.txt}</h1>
  )
}

export default MoonH1