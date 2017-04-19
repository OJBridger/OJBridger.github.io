document.getElementById('changeColor').addEventListener('click', function() {
    var color = document.getElementById('backgroundColor').value;
    var body = document.getElementById('body');
    body.style.background = color;
    
    console.log('body', body);
    console.log('Clicked!');
});
