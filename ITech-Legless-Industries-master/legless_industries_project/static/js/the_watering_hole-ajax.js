$(document).ready(function() {

 $('#likes').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
     $.get("/the_watering_hole/like_review/", {review_id: catid}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
           });
});

});