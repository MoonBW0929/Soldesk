function reg_consumption(){

    $("#btn_reg").click(function(){

        var price = $("#input_price").val();
        var detail = $("#input_detail").val();
        var date = $("#input_date").val();
        var url = "http://195.168.9.125:4567/consumption.reg?";
        url += "price="+price+"&detail="+detail+"&date="+date;

        $.getJSON(url, function(result){

            if(result.execute_ok == true) alert("등록 성공");
            else alert("등록 실패");
        });
    });
}

function get_consumption(){

    $(".search").click(function(){
        
        if($(this).attr("id") == "a_next") {
            if(page < max_page) page++;
        }
        else if($(this).attr("id") == "a_prev") {
            if(page > 1) page--;
        }

        var url = "http://195.168.9.125:4567/consumption.get?";
        url += "page="+page
        
        $.getJSON(url, function(result){
            
            if(result.execute_ok == false) alert("조회에 실패하였습니다");
            else {
                
                $("#search_footer").find("h1").text(page+" / "+result.month_cnt);
                max_page = result.month_cnt;
                
                $("#search_listview").empty();
                var month = 0;

                for(data of result.consumption){

                    var li, a, div;

                    if(month != +(data.date.substring(4, 6))){

                        li = $("<li></li>");
                        $(li).text(data.date.substring(0, 4)+"년 "+data.date.substring(4, 6)+"월 내역");
                        $(li).attr("data-role", "list-divider");
                        
                        $("#search_listview").append(li).listview("refresh");
                        
                        month = +(data.date.substring(4, 6));
                    }
                    
                    li = $("<li></li>");
                    div = $("<div></div>");
                    $(div).css("display", "none").text(data.no);
                    a = $("<a></a>");
                    $(a).html(data.date.substring(6, 8)+"일"+"<br>"+"-"+data.price+" / "+data.detail);
                    $(a).attr("href", "#p1_detail");
                    $(a).append(div);

                    $(a).click(function() {
                
                        $("#search_detail_listview").empty();

                        var url = "http://195.168.9.125:4567/consumption.search.detail?";
                        url += "no="+$(this).children().text();

                        $.getJSON(url, function(result){

                            if(result.execute_ok == false) alert("조회에 실패하였습니다");
                            else {

                                for(data of result.consumption){
                                    
                                    var y = data.date.substring(0, 4);
                                    var M = data.date.substring(4, 6);
                                    var d = data.date.substring(6, 8);
                                    var h = data.date.substring(9, 11);
                                    var m = data.date.substring(11, 13);
                                    var date = "&nbsp;&nbsp;"+y+"년 "+M+"월 "+d+"일  "+h+":"+m;

                                    $("#detail_name").html(data.detail);
                                    $("#detail_date").html(date);
                                    $("#detail_price").html("- "+data.price+" 원");

                                    $("#h_div").text(data.no);
                                }
                            }
                        });

                    });

                    $(li).append(a);

                    $("#search_listview").append(li).listview("refresh");
                }
            }
        });
    });
}


function search_consumption(){
    
    $("#search_input").keyup(function(evt){

        var keyword = $(this).val();

        if(keyword == ""){
            page = 1;
            $("#a_search").click();
        }
        else{

            $("#search_footer h1").text("");

            var url = "http://195.168.9.125:4567/consumption.search?";
            url += "keyword="+keyword;
            
            $.getJSON(url, function(result){
                
                if(result.execute_ok == false) alert("조회에 실패하였습니다");
                else {
                    
                    $("#search_listview").empty();
                    var month = 0;
    
                    for(data of result.consumption){
    
                        var li, a, div;
    
                        if(month != +(data.date.substring(4, 6))){
                            li = $("<li></li>");
                            $(li).text(data.date.substring(0, 4)+"년 "+data.date.substring(4, 6)+"월 내역");
                            $(li).attr("data-role", "list-divider");
    
                            $("#search_listview").append(li).listview("refresh");
    
                            month = +(data.date.substring(4, 6));
                        }
    
                        li = $("<li></li>");
                        div = $("<div></div>");
                        $(div).css("display", "none").text(data.no);
                        a = $("<a></a>");
                        $(a).html(data.date.substring(6, 8)+"일"+"<br>"+"-"+data.price+" / "+data.detail);
                        $(a).attr("href", "#p1_detail");
                        $(a).append(div);

                        $(a).click(function() {
                    
                            $("#search_detail_listview").empty();

                            var url = "http://195.168.9.125:4567/consumption.search.detail?";
                            url += "no="+$(this).children().text();

                            $.getJSON(url, function(result){

                                if(result.execute_ok == false) alert("조회에 실패하였습니다");
                                else {

                                    for(data of result.consumption){
                                        
                                        var y = data.date.substring(0, 4);
                                        var M = data.date.substring(4, 6);
                                        var d = data.date.substring(6, 8);
                                        var h = data.date.substring(9, 11);
                                        var m = data.date.substring(11, 13);
                                        var date = "&nbsp;&nbsp;"+y+"년 "+M+"월 "+d+"일  "+h+":"+m;

                                        $("#detail_name").html(data.detail);
                                        $("#detail_date").html(date);
                                        $("#detail_price").html("- "+data.price+" 원");
                                    }
                                }
                            });

                        });

                        $(li).append(a);

                        $("#search_listview").append(li).listview("refresh");
                    }
                }
            });
        }
    });
}


function delete_consumption(){

    $("#btn_delete").click(function(){

        var no = $("#h_div").text();

        var url = "http://195.168.9.125:4567/consumption.del?";
        url += "no="+no;

        $.getJSON(url, function(result){

            if(result.execute_ok == true) alert("삭제 성공");
            else alert("삭제 실패");

            $("#a_search").click();
        });
    });
}

function modify_consumption(){

    $("#btn_goto_modify").click(function (){

        $.mobile.changePage("#p1_modify");

        $("#modify_detail").val($("#detail_name").text());
        end = $("#detail_price").text().indexOf("원") - 1;
        $("#modify_price").val($("#detail_price").text().substring(2, end));
        
        // yyyy-mm-ddThh:MM
        var y = $("#detail_date").text().substring(2, 6);
        var m = $("#detail_date").text().substring(8, 10);
        var d = $("#detail_date").text().substring(12, 14);
        var h_m = $("#detail_date").text().substring(17, 22);
        var date = y+"-"+m+"-"+d+"T"+h_m;

        $("#modify_date").val(date);

    });

    $("#btn_modify").click(function (){

        var no = $("#h_div").text();
        var detail = $("#modify_detail").val();
        var price = $("#modify_price").val();
        var date = $("#modify_date").val();

        alert(date);

        var url = "http://195.168.9.125:4567/consumption.mdf?";
        url += "no="+no+"&detail="+detail+"&price="+price+"&date="+date;

        // $.getJSON(url, function(result){

        //     if(result.execute_ok == true) alert("수정 성공");
        //     else alert("수정 실패");

        //     $("#a_search").click();
        // });
    });
}

function scroll_event(){

    var html_height = $(document).height();
    var brower_height = $(window).height();
    var brower_offsetTop = $(window).scrollTop();
    var brower_offsetBottom = brower_offsetTop + brower_height;

    if(brower_offsetBottom >= html_height - 20){
        // alert("z");
    }
}

var page = 1;
var max_page;

$(function(){

    reg_consumption();
    get_consumption();
    search_consumption();
    delete_consumption();
    modify_consumption();
    scroll_event();

    $(".a_back_main").click(function (){
        page = 1;
        $("#search_input").val("");
    });
});