import $ from 'jquery'
import selectize from 'selectize'
import barrating from 'jquery-bar-rating'

import 'selectize/dist/css/selectize.css'
import 'jquery-bar-rating/dist/themes/bars-square.css'
import '../css/fixes.css'

$( function () {
  $('#id_tags').selectize()
  $('#id_categories').selectize()
  $('#id_rating').barrating('show', {
    theme: 'bars-square',
    showValues: true,
    showSelectedRating: false
  })
})
