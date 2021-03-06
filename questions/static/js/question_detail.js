﻿$(function () {
    BindEventListeners();
});
function BindEventListeners() {
    $("#vote_question_up").on("click.vote", function () {
        $(this).addClass("vote_up vote_off");
        var questionId = +$(this).data('questionid');
        var that = this;
        increment_score(questionId).done(function (e) {
            $("#question_score").text(e.score);
            $(that).off("click.vote");
        });
    });
    $("#vote_question_down").on("click.vote", function () {
        $(this).addClass("vote_up vote_off");
        var questionId = +$(this).data('questionid');
        var that = this;
        decrement_score(questionId).done(function (e) {
            $("#question_score").text(e.score);
            $(that).off("click.vote");
        });
    });
}
function increment_score(question_id) {
    return $.ajax({
        method: 'POST',
        url: '/add_score/' + question_id + ''
    })
}
function decrement_score(question_id) {
    return $.ajax({
        method: 'POST',
        url: '/sub_score/' + question_id 
    })
}