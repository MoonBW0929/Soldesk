import { createSlice } from '@reduxjs/toolkit'

const initialState = {
    txt : "",
}

const MoonTxtSlice = createSlice({
  name: "mts",
  initialState,
  reducers: {
    set_text : (c_state, action) => {
        c_state.txt = action.payload;
    }
  }
});

export const {set_text} = MoonTxtSlice.actions

export default MoonTxtSlice.reducer