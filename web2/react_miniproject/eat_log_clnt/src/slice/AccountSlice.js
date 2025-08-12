import { createSlice } from "@reduxjs/toolkit";

const initialState = {
    login: false,
    left: "",
    top: "",
    updateProfile: false,
};

const AccountSlice = createSlice({
    name: "ls",
    initialState,
    reducers: {
        set_login: (c_state, action) => {
            c_state.login = action.payload;
        },
        set_size: (c_state, action) => {
            c_state.left = action.payload.left;
            c_state.top = action.payload.top;
        },
        set_profile: (c_state, action) => {
            c_state.updateProfile = action.payload;
        }
    },
});

export const { set_login, set_size, set_profile } = AccountSlice.actions;

export default AccountSlice.reducer;
