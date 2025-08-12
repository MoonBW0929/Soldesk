function input_empty_check(field){
    return !field.value;
}

function input_MinLength_check(len, field){
    return (len > field.value.length);
}

function input_Available_check(field){
 
    var char = "abcdefghijklmnopqrstuvwxyz";
    char += "ABCDEFGHIJKLMNOPQRSTUVWZYZ";
    char += "1234567890";
    char += "-_.@#";

    for(var i = 0; i < field.value.length; i++){
        if(char.indexOf(field.value[i]) == -1){
            return true;
        }
    }

    return false;
}

function input_equal_check(field1, field2){
    return !field1.value == field2.value;
}

function input_contain_check(set, field){

    for(var i = 0; i < set.length; i++){
        if(field.value.indexOf(set[i]) != -1){
            return false;
        }
    }

    return true;
}

function input_onlyNum_check(field){
    return isNaN(field.value) || (field.value.indexOf(" ") != -1);
}

function input_file_check(file_type, field){
    file_type = "." + file_type;
    return field.value.toLowerCase().indexOf(file_type) == -1;
}

function input_onlyPhoto_check(field){
    var check = true;
    check &= input_file_check("jpg", field);
    check &= input_file_check("gif", field);
    check &= input_file_check("png", field);
    check &= input_file_check("bmp", field);

    return check;
}