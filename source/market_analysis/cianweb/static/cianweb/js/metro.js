document.getElementById('id_city').addEventListener('change', function(){
    var city_id = this.value;
    $.ajax({
        type: 'GET',
        url: 'get_metro/',
        data: {'city': city_id },
        dataType: 'json',
        success: function(data){
            var select = document.getElementById("id_metro")
            select.innerHTML = '';

            data.forEach(function(metro){
                var option = document.createElement('option');
                option.value = metro.id;
                option.text = metro.name;
                select.appendChild(option);
            });
        }
    });
});
