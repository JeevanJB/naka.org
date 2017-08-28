$(document).ready(function(){

	$('#myModal').on('show.bs.modal', function () {
   $('.page-wrapper').addClass('blur');
})

$('#myModal').on('hide.bs.modal', function () {
   $('.page-wrapper').removeClass('blur');
})

		if($('.tabs-box').length){
		$('.tabs-box .tab-buttons .tab-btn').on('click', function(e) {
			e.preventDefault();
			var target = $($(this).attr('data-tab'));

			if ($(target).is(':visible')){
				return false;
			}else{
				target.parents('.tabs-box').find('.tab-buttons').find('.tab-btn').removeClass('active-btn');
				$(this).addClass('active-btn');
				target.parents('.tabs-box').find('.tabs-content').find('.tab').fadeOut(0);
				target.parents('.tabs-box').find('.tabs-content').find('.tab').removeClass('active-tab');
				$(target).fadeIn(300);
				$(target).addClass('active-tab');
			}
		});
	}
	if($('.main-header').length){
			$(window).scroll(function (event) {
				var siteHeader = $('.main-header');
				var scrollLink = $('.scroll-to-top');
				var windowpos = $(window).scrollTop();
				if (windowpos >= 200) {
				siteHeader.addClass('fixed-header');
				scrollLink.fadeIn(300);

			} else {
				siteHeader.removeClass('fixed-header');
				scrollLink.fadeOut(300);
				//alert('aa');
			}
			});

		}

		var menuWrap = $('.hidden-bar .side-menu');
		// appending expander button
		menuWrap.find('.dropdown').children('a').append(function () {
			return '<button type="button" class="btn expander"><i class="icon fa fa-angle-down"></i></button>';
		});
		// hidding submenu
		menuWrap.find('.dropdown').children('ul').hide();
		// toggling child ul
		menuWrap.find('.btn.expander').each(function () {
			$(this).on('click', function () {
				$(this).parent() // return parent of .btn.expander (a)
					.parent() // return parent of a (li)
						.children('ul').slideToggle();

				// adding class to expander container
				$(this).parent().toggleClass('current');
				// toggling arrow of expander
				$(this).find('i').toggleClass('fa-angle-up fa-angle-down');

				return false;

			});
		});


		var hiddenBar = $('.hidden-bar');
		var hiddenBarOpener = $('.hidden-bar-opener');
		var hiddenBarCloser = $('.hidden-bar-closer');


		//Show Sidebar
		hiddenBarOpener.on('click', function () {
			hiddenBar.addClass('visible-sidebar');
		});

		//Hide Sidebar
		hiddenBarCloser.on('click', function () {
			hiddenBar.removeClass('visible-sidebar');
		});
});

function signUp(){
	$("#signUp1").css("display", "block");
	$("#login1").css("display", "none");

	}

	function login(){
	$("#signUp1").css("display", "none");
	$("#forget").css("display", "none");
	$("#login1").css("display", "block");

	}

	function forget(){
	$("#forget").css("display", "block");
	$("#login1").css("display", "none");

	}
