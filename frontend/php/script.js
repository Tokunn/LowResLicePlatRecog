$(function(){
    $("#preres").text("Generate IMG");

    $('#genimgnum').on("keydown", function(e) {
        if(e.keyCode === 13) {
            $("#genimg").trigger("click");
        }
    });

    $('#genimg').click(function() {
        $("#preres").text("Generating...");
        $("ul").text("");
        var param_genimgnum = $('#genimgnum').val();
        $.ajax({
            type: "POST",
            url: "./action.php",
            data: {
                "genimgnum": param_genimgnum
            },
            success: function(j_data){
                var dataArray = $.parseJSON(j_data);
                $.each(dataArray, function(i) {
                    $.each(dataArray[i], function(key, name) {
                        var url = "./imgs/" + i + "/" + name;
                        var addcode = "<li id= " +
                            url.split(".").join("").split("/").join("") +
                            "><img src=" + url + " width=72 alt=" + url +
                            " class=ChangePhoto></li>";
                        $("ul").append(addcode);
                    });
                });
                $("#preres").text("Chose IMG");

                $('img.ChangePhoto').click(function() {
                    var ImgSrc = $(this).attr("src");
                    var ImgAlt = $(this).attr("alt");
                    var ImgId = ImgSrc.split(".").join("").split("/").join("") 
                    $("img#MainPhoto").attr({src:ImgSrc, alt:ImgAlt});
                    $("img#MainPhoto").hide();
                    $("img#MainPhoto").fadeIn("slow");
                    $("li#" + ImgId).attr({class:"selected_img"});
                    //$("#debug").append("li#" + ImgId);
                    $("#preres").text("Predicting... [" + ImgSrc.slice(7, 11) + "]");
                    $.ajax({
                        type: "POST",
                        url: "./action.php",
                        data: {
                            "predictimg": ImgSrc
                        },
                        success: function(predicted) {
                            $("#preres").text("Predict : " + predicted + " [" + ImgSrc.slice(7, 11) + "]");
                        }
                    });
                });
            }
        });
    });
});
