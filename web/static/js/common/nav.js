function confirmLogout() {
    if( confirm("Are you sure you want to log out?") ) {
        location.href = "/logout";
    }
}


//클릭시 유저정보 팝업
$(function() {
    $('.userInfo').click(function() {
        $('.userInfoOpen').show();
    });
    $('.userInfoClose').click(function() {
        $('.userInfoOpen').hide();
    });
})







