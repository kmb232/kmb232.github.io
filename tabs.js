$(document).ready(function() {
  $("ul.box_div a").on("click", function(e) {
    // The `target` field of the event is a reference to the link
    // that was clicked on
    var link = e.target;
    // We want to get the link `href` attribute and remove the
    // leading `#` character
    var href = link.getAttribute("href").slice(1);
    // We build up the selector string by inserting the `href` we
    // got earlier into the `name` filter for the `a` tags, and 
    // use jQuery to find the specific element
    var anchorSelector = "a[name='" + href + "']";
    var $anchor = $(anchorSelector);
    // Now, select all the `div` elements whose `id`s start with
    // 'topic' and ensure they're all hidden
    $("div[id^='topic'").hide();
    // Finally, find the containing topic div and fade it in
    $anchor.parent().parent().fadeIn();
    // Now inhibit the link from jumping to focus on the div
    return false;
  });
});

$(document).ready(function(){
    $("#close").click(function(){
        $("div[id^'topic'").hide();
    });
}); 