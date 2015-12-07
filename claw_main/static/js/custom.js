
// jQuery script for are Circle div whit Scroll Reveal Script

$(document).ready(function(){

    $(".squere").click(function(){
        $(".content").hide(800);
        $(".squere").removeClass("active");
        $(this).addClass("active");
    $(this).next(".content").slideDown(1000);
    });

    /*==========================================
    SCROLL REVEL SCRIPTS
    =====================================================*/


            window.scrollReveal = new scrollReveal();


});

/* A key/value dictionary for texts to be displayed.
 * The keys are paired with each image's alt attribute. 
 */
var texts = {
  "default_title" : "Default title",
  "default_description" : "Default description",
  "item1_title" : "Item 1 title",
  "item1_description" : "Item 1 description",
  "item2_title" : "Item 2 title",
  "item2_description" : "Item 2 description",
  "item3_title" : "Item 3 title",
  "item3_description" : "Item 3 description",
  "item4_title" : "Item 4 title",
  "item4_description" : "Item 4 description",
  "item5_title" : "Item 5 title",
  "item5_description" : "Item 5 description",
  "item6_title" : "Item 6 title",
  "item6_description" : "Item 6 description",
  "item7_title" : "Item 7 title",
  "item7_description" : "Item 7 description",
  "item8_title" : "Item 8 title",
  "item8_description" : "Item 8 description",
}


$(document).ready(function(){
  
  /* If you don't want the texts to revert back to its original state, simply remove the mouseleave part */
  $('body').on({ 
    mouseenter : function(event){
      var item_alt = $(event.target).attr("alt");
      $("#item_title").html(texts[item_alt+"_title"]);
      $("#item_description").html(texts[item_alt+"_description"]);
    }, 
      mouseleave : function(event){
      $("#item_title").html(texts["default_title"]);
      $("#item_description").html(texts["default_description"]);
    }
  }, ".moon");
});
