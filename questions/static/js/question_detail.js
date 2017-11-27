$(function () {
    BindEventListeners();
});
function BindEventListeners() {
    $("#vote_question_up").click(function () {
        $(this).addClass("vote_up vote_off");
        var questionId = +$(this).data('questionid');
        increment_score(questionId);
    })
    $("#vote_question_down").click()
}
function increment_score(question_id) {

    $.ajax({
        method: 'POST',
        url: '/questions/' + question_id + '/add_score'
    }).success(function (e) {
        console.log(e);
    }).failure(function (e) {
        console.error(e);
    })
}