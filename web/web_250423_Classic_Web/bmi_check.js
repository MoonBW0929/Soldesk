function check(){

    var name = document.main_form.name;
    var height = document.main_form.height;
    var weight = document.main_form.weight;
    var photo = document.main_form.photo;
    var check = true;

    if(input_empty_check(name)){
        alert("이름?")
        check = false;
    }

    if(input_empty_check(height) || input_onlyNum_check(height)){
        alert("키?")
        check = false;
    }
    
    if(input_empty_check(weight) || input_onlyNum_check(height)){
        alert("몸무게?")
        check = false;
    }

    if(input_empty_check(photo) || input_onlyPhoto_check(photo)){
        alert("사진?")
        check = false;
    }

    return check;
}