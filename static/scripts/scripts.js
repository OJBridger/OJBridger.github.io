$(function() {
  populatePosts();
});

function populatePosts()  {
  $.ajax({
    url: '/posts'
  }).done(function(response) {
    var template = $('#post-template').html();
    response.forEach(function(post) {
      console.log('>>post', post);
      var newPost = $(template).clone();
      $(newPost).find('.title').html(post[0]);
      $(newPost).find('.post').html(post[1]);
      $(newPost).find('.likes').html(post[2]);
      $(newPost).find('.like-button').on('click', function() {
        console.log("Clicked");
        $.ajax({
          url: '/like/' + post[3]
        }).done(function() {
          $(newPost).find('.likes').html(++post[2])
        });        
      });
      $('#post-list').append(newPost);
    });
  });
}

