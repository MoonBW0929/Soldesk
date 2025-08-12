function array_test(){
    var a = [10, 12, 31, 24, 55];

    // for(var i = 0; i < a.length; i++){
    //     alert(a[i]);
    // }

    for(var v of a){
        alert(v)
    }
}

function object_test(){
    var d = {name:"후추", age:3}
    alert(d);
    alert(d.name);
    alert(JSON.stringify(d))
}

function ao_test(){
    var dogs = [
        {name:"후추", age:3},
        {name:"복슬이", age:1},
        {name:"초코", age:2}
    ];

    for(var dog of dogs){

        alert(dog.name + " : " + dog.age);
    }
}