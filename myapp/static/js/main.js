$(function(){
    $('.showMore').slideUp()
    $('.seeMore').click(function(event){
        console.log('ok')
        $('.showMore').slideToggle();
        $(this).toggleClass('minus')
    })
})