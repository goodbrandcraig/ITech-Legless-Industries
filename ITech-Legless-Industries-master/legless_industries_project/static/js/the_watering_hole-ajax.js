$(document).ready(function() {

 $('button.btn-mini').click(function(){
     var catid = $(this).attr("data-catid");
     $.get("/the_watering_hole/like_review/", {review_id: catid}, function(data){
               var buttonId = "likes_"+catid;
               var likeCountId = "like_count_"+catid;
               $('#'+likeCountId).html(data);
               $('#'+buttonId).hide();
      });
 });
});