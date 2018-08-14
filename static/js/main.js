$(function() {
  $('.ui.checkbox').checkbox();
  $('.ui.dropdown,.ui.dropdown.-type-arrow').dropdown();
  renderDataTable();
  validateForm();
  objFit();
  typePhoto();
});

function typePhoto(){
  $('body').on('click','.photo-btn',function(){
    $('.photo-btn').removeClass('isActive');
    $(this).addClass('isActive');
    console.log('click type');
  });
}

function validateForm(){
  $('.ui.form')
    .form({
      // on     : 'blur',
      // inline: true,
      fields: {
        title: {
          identifier: 'title',
          rules: [
            {
              type : 'empty',
            }
          ]

        },

        anno: {
          identifier: 'anno',
          rules: [
            {
              type: 'regExp',
              value: /(19[789]\d|20[01]\d)/,
            }
          ]
        },

        DescrizioneBreve: {
          identifier: 'DescrizioneBreve',
          rules: [
            {
              type : 'empty',
            }
          ]
        },

        Descrizione: {
          identifier: 'Descrizione',
          rules: [
            {
              type : 'empty',
            }
          ]
        },

        Categorie: {
          identifier: 'Categorie',
          rules: [
            {
              type : 'empty',
            }
          ]
        },

        tags: {
          identifier: 'tags',
          rules: [
            {
              type : 'empty',
            }
          ]
        },

        locchi: {
          identifier: 'locchi',
          rules: [
            {
              type : 'empty',
            }
          ]
        },

        luogo: {
          identifier: 'luogo',
          rules: [
            {
              type : 'empty',
            }
          ]
        },

        creative: {
          identifier: 'creative',
          rules: [
            {
              type: 'checked',
            }
          ]
        },

        immagine: {
          identifier: 'immagine',
          rules: [
            {
              type: 'checked',
            }
          ]
        },

        rating: {
          identifier: 'rating',
          rules: [
            {
              type: 'checked',
            }
          ]
        },

      }
    });
}

$('body').on('click','.b-tags a.visible', function(e){
  e.preventDefault();

  var starValue = $(this).find('.tag i').attr('data-value');
  switch(starValue) {
    case '0':
      $(this).find('.tag i').attr('data-value','1');
      $(this).find('.tag i').removeClass().addClass('fa fa-star-half-o');
      break;
    case '1':
      $(this).find('.tag i').attr('data-value','2');
      $(this).find('.tag i').removeClass().addClass('fa fa-star');
      break;
    case '2':
      $(this).find('.tag i').attr('data-value','0');
      $(this).find('.tag i').removeClass().addClass('fa fa-star-o');
      break;
  }

});

function objFit(){
  if ('objectFit' in document.documentElement.style === false) {
    document.addEventListener('DOMContentLoaded', function () {
      Array.prototype.forEach.call(document.querySelectorAll('img[data-object-fit]'), function (image) {
        (image.runtimeStyle || image.style).background = 'url("' + image.src + '") no-repeat 50%/' + (image.currentStyle ? image.currentStyle['object-fit'] : image.getAttribute('data-object-fit'));

        image.src = 'data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' width=\'' + image.width + '\' height=\'' + image.height + '\'%3E%3C/svg%3E';
      });
    });
  }
}

function renderDataTable(){
  $('#example tfoot th').each( function () {
    var title = $(this).text();
    if(title !== 'thumb' && title !== 'edit'){
      $(this).html( '<input type="text" placeholder="Search '+title+'" />' );
    }

  } );

  // DataTable
  var table = $('#example').DataTable();

  // Apply the search
  table.columns().every( function () {
    var that = this;

    $( 'input', this.footer() ).on( 'keyup change', function () {
      if ( that.search() !== this.value ) {
        that
          .search( this.value )
          .draw();
      }
    } );
  } );
}