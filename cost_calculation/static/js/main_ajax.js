$(function ($){
    $('#form_ajax').submit(function (e) {
        e.preventDefault()
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            dataType: 'json',
            success: function (response) {
                document.getElementById("text_cost").textContent=response.text;
            },
        })
    })
})