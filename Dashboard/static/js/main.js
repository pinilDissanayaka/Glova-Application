(function ($) {
    "use strict";
    // Sidebar Toggler
    $('.sidebar-toggler').click(function () {
        $('.sidebar, .content').toggleClass("open");
        return false;
    });    
})(jQuery);

function previewFile(input){
    var file = $("input[type=file]").get(0).files[0];

    if(file){
        var reader = new FileReader();

        reader.onload = function(){
            $(".img-thumbnail").attr("src", reader.result);
        }

        reader.readAsDataURL(file);
    }
}


