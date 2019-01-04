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
    plugins: ['remove_button'],
    render: {
        option_create: function(data, escape) {
          return '<div class="create" style="line-height: 2rem; vertical-align: middle; height: 2rem; font-size: 1.5rem;">Add <strong>' + escape(data.input) + '</strong>&hellip;</div>';
        }
    },
    create:function (input, callback){
        $.ajax({
            url: '/administration/add-tag/',
            type: 'POST',
            data: {"input": input},
            xhrFields: {
              withCredentials: true
            },
            success: function (result) {
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
  $('#id_place').selectize({
    plugins: ['remove_button'],
  });
  $('#id_categories').selectize({
    plugins: ['remove_button'],
  });
  $('#id_rating').barrating('show', {
    theme: 'bars-square',
    showValues: true,
    showSelectedRating: false
  });
  $(".delete-button").on("click", function(e) {
    e.preventDefault();
    if (confirm('Are you sure?')) {
        $.post({
            url: $( this ).attr('href'),
            xhrFields: {
              withCredentials: true
           }
        }).done(function(data) {
           if ('url' in data) {
             location.replace(data['url']);
           }
           if ('error' in data) {
             alert(data['error']);
           }
        });
    }
  });
  $('#compile_image_data').on('click', function(e) {
    e.preventDefault();
    var data = window.fotolocchi_image_data;
    if (data) {
        $.each(["title", "short_description", "full_description", "archive", "notes", "day", "month", "year", "support", "shop_link", "status"], function(index, field_name) {
            $('#id_' + field_name).val(data[field_name]);
        });

        $.each(["place", "tags", "categories"], function(index, field_name) {
            var selectizer = $('#id_' + field_name).data('selectize');
            selectizer.setValue(data[field_name]);
        });
        $("#id_rating").barrating('set', data['rating']);

        $.each(["creative", "is_publish", "is_decennary"], function(index, field_name) {
            $('#id_' + field_name).prop('checked', data[field_name]);
        });

        $('#id_scope [value='+ data['scope'] + ']').click();
    }
  });
})
