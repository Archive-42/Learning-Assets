jQuery( function ( t ) {
  if ( t( ".search-button" ).on( "click", function () {
      t( ".search-overlay" ).toggleClass( "search-overlay-visible" ), t( ".search-overlay" ).one( "transitionend", function () {
        t( ".search-field" ).focus()
      } )
    } ), t( ".search-overlay-close" ).on( "click", function () {
      t( ".search-overlay" ).toggleClass( "search-overlay-visible" )
    } ), t( document ).keyup( function ( e ) {
      27 == e.keyCode && 1 == t( ".search-overlay" ).css( "opacity" ) && t( ".search-overlay" ).removeClass( "search-overlay-visible" )
    } ), t( ".post-full-content" ).fitVids(), t( ".single-post" ).length ) {
    var n = document.querySelector( "#reading-progress" ),
      i = document.querySelector( ".floating-header" ),
      s = document.querySelector( ".post-full-title" ),
      r = window.scrollY,
      c = window.innerHeight,
      l = t( document ).height(),
      a = !1;

    function e() {
      a || requestAnimationFrame( o ), a = !0
    }

    function o() {
      var e = s.getBoundingClientRect().top + window.scrollY,
        t = s.offsetHeight + 35,
        o = l - c;
      e + t <= r ? i.classList.add( "floating-active" ) : i.classList.remove( "floating-active" ), n.setAttribute( "max", o ), n.setAttribute( "value", r ), a = !1
    }
    s && ( window.addEventListener( "scroll", function () {
      r = window.scrollY, e()
    }, {
      passive: !0
    } ), window.addEventListener( "resize", function () {
      c = window.innerHeight, l = t( document ).height(), e()
    }, !1 ), o() )
  }
} );;
