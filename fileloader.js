var code = $("#code");
$("#dropdown").load("nav.html", function() {
    var file = $(".file");

    file.click(function () {
        code.load(this.id, function() {
            Prism.highlightElement(code[0]);
        });
    });
});

$('#brand').click(splash);

function splash() {
    code.load('splash.html')
}
splash();