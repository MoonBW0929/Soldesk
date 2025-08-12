import { createSlice } from "@reduxjs/toolkit";

const initialState = {
    fontSize: 30,
};

const MoonSizeSlice = createSlice({
    name: "slice",
    initialState,
    reducers: {
        bigger: (c_state) => {
            c_state.fontSize += 10;
        },
        smaller: (c_state) => {
            if (c_state.fontSize > 10) c_state.fontSize -= 10;
        },
    },
});

export const { bigger, smaller } = MoonSizeSlice.actions;

export default MoonSizeSlice.reducer;
