function a(){
    var name = document.getElementById("name_input");
    var age = document.getElementById("age_input");

    location.href = "http://195.168.9.125/te.st?name=" + name.value +
                    "&age=" + age.value;
}