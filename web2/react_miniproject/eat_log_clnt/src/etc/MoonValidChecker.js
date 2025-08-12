import axios from "axios"

export const empty_check = (txt) => {
    return txt === "";
}

export const minLen_check = (txt, len) => {
    return (txt.length < len)
}

export const available_check = (txt) => {
    var char = "abcdefghijklmnopqrstuvwxyz";
    char += "ABCDEFGHIJKLMNOPQRSTUVWZYZ";
    char += "1234567890";
    char += "-_.@#";

    for(var i = 0; i < txt.length; i++){
        if(char.indexOf(txt[i]) === -1){
            return true;
        }
    }

    return false;
}

export const equal_check = (txt1, txt2) => {
    return !(txt1 === txt2);
}

export const contain_check = (txt, set) => {

    for(var i = 0; i < set.length; i++){
        if(txt.indexOf(set[i]) !== -1){
            return false;
        }
    }

    return true;
}

export const onlyNum_check = (txt) => {
    return !isNaN(txt) || (txt.indexOf(" ") !== -1);
}

export const file_check = (file, file_type) => {
    file_type = "." + file_type;
    return file.name.toLowerCase().indexOf(file_type) === -1;
}

export const onlyPhoto_check = (file) => {
    let check = true;
    check &= file_check(file, "jpg");
    check &= file_check(file, "gif");
    check &= file_check(file, "png");
    check &= file_check(file, "bmp");

    return check;
}

export const duplicate_check = async (txt, type) => {
    
    let result;
    
    await axios
        .get(
            `http://195.168.9.125:4567/account.duplicate?txt=${txt}&type=${type}`
        )
        .then((res) => {
            result = res.data.result
        })

    if(result) return false;
    else return true;
}