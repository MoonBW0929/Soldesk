function check(){

    var id_field = document.joinform.id_field;
    var pw_field = document.joinform.pw_field;
    var re_pw_field = document.joinform.re_pw_field;
    var age_field = document.joinform.age_field;
    var photo_field = document.joinform.photo_field;

    check = true

    if(input_empty_check(id_field) || input_MinLength_check(4, id_field) || input_Available_check(id_field)){
        alert("ID?");
        id_field.focus();
        id_field.value = "";
        check = false;
    }
    
    var set = [];
    set[0] = "abcdefghijklmnopqrstuvwxyz";
    set[1] = "ABCDEFGHIJKLMNOPQRSTUVWZYZ";
    set[2] = "1234567890";
    set[3] = "-_.@#!";
    set[4] = "abc123";
    set[5] = "!@#iop";

    if(input_empty_check(pw_field) || input_MinLength_check(5, pw_field) 
        || input_equal_check(pw_field, re_pw_field) 
        || input_contain_check(set[0], pw_field) || input_contain_check(set[2], pw_field)){
        alert("PW?");
        pw_field.focus();
        pw_field.value = "";
        re_pw_field.value = "";
        check = false;
    }

    if(input_empty_check(age_field) || input_onlyNum_check(age_field)){
        alert("나이?");
        age_field.focus();
        age_field.value = "";
        check = false;
    }

    
    if(input_empty_check(photo_field) || input_onlyPhoto_check(photo_field)){
        alert("프사?");
        age_field.value = "";
        check = false;
    }

    return check;
}