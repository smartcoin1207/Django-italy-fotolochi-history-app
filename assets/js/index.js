import $ from 'jquery'
import selectize from 'selectize'
import barrating from 'jquery-bar-rating'

import 'selectize/dist/css/selectize.css'
import 'jquery-bar-rating/dist/themes/bars-square.css'
import 'bulma-divider/dist/css/bulma-divider.min.css'
import '../css/fixes.css'

$( function () {
  var csrftoken = $("[name=csrfmiddlewaretoken]").val();
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
       if (settings.type == 'POST' && !this.crossDomain) {
         xhr.setRequestHeader("X-CSRFToken", csrftoken);
       }
    }
  });
  $('#id_tags').selectize({
    create:function (input, callback){
        console.log($.fn.jquery);
        $.ajax({
            url: '/administration/add-tag/',
            type: 'POST',
            data: {"input": input},
            xhrFields: {
              withCredentials: true
            },
            success: function (result) {
                console.log("SUC", result);
                if (result) {
                    callback({ value: result.id, text: input });
                }
            },
            error: function (result) {
                console.log("ERR", result);
            }
        });
    }
  });
  $('#id_place').selectize();
  $('#id_categories').selectize();
  $('#id_rating').barrating('show', {
    theme: 'bars-square',
    showValues: true,
    showSelectedRating: false
  });
  $(".delete-button").on("click", function(e) {
    e.preventDefault();
    if (confirm('Are you sure?')) {
        console.log( $( this ).attr('href') );
        $.post({
            url: $( this ).attr('href'),
            xhrFields: {
              withCredentials: true
           }
        }).done(function(data) {
           location.reload(true);
        });
    }
  });
})
