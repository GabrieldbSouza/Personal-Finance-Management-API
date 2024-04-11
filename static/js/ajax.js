$(document).ready(function () {
    $("#loginBtn").click(function () {
        $("#content").load("/login/");
    });

    $("#registerBtn").click(function () {
        $("#content").load("/register/");
    });

    $("#form_transBtn").click(function () {
        var segments = window.location.pathname.split('/');
        var user_id = segments.pop();
        if (user_id === '') {
            user_id = segments.pop();
        }
        
        console.log(user_id);

        $("#content").load("/user/" + user_id + "/transaction/new/");
    });

    $("#transBtn").click(function (table) {
        var segments = window.location.pathname.split('/');
        var user_id = segments.pop();
        if (user_id === '') {
            user_id = segments.pop();
        }
        $("#content2").load("/user/" + user_id + "/transaction/html");
        // Carrega os dados das transações quando o documento estiver pronto
        $.get("/user/" + user_id + "/transaction/data", function(data) {
            // Limpa o corpo da tabela
            $("#transactionTable tbody").empty();
            // Preenche a tabela com os dados recebidos
            data.forEach(function(transaction) {
                var row = $("<tr>");
                $("<td>").text(transaction.id).appendTo(row);
                $("<td>").text(transaction.trans_user_id).appendTo(row);
                $("<td>").text(transaction.date).appendTo(row);
                $("<td>").text(transaction.amount).appendTo(row);
                row.appendTo("#transactionTable tbody");
            });
        });
    });

    $("#formLogin").submit(function (event) {
        event.preventDefault();
        var email = $("#emailInput").val();
        var password = $("#passwordInput").val();
        $.ajax({
            url: "/login",
            type: "POST",
            data: {
                email: email,
                password: password
            }
        });
    });
    
    function loadChart() {
        var segments = window.location.pathname.split('/');
        var user_id = segments.pop();
        if (user_id === '') {
            user_id = segments.pop();
        }
        $.get("/user/" + user_id + "/transaction/chartjs", function(data) {
            
            data.sort(function(a, b) {
                return new Date(a.date) - new Date(b.date);
            });
            var labels = [];
            var amounts = [];
            data.forEach(function(transaction) {
                labels.push(transaction.date);
                amounts.push(transaction.amount);
            });

            var ctx = document.getElementById('myChart').getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Transactions',
                        data: amounts,
                        backgroundColor: 'rgba(255, 99, 132, 0.2)',
                        borderColor: 'rgba(255, 99, 132, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    },
                    responsive: false, // Torna o gráfico responsivo
                    maintainAspectRatio: false, // Permite definir o tamanho do gráfico manualmente
                    aspectRatio: 2, // Define a relação de aspecto do gráfico
                    layout: {
                        padding: {
                            left: 20,
                            right: 20,
                            top: 20,
                            bottom: 20
                        }
                    }
                }
            });
        });
    }
    $("#content2").click(function (){
        table();
    });
    // Carrega o gráfico quando o documento estiver pronto
    $("#chartjs").click(function () {
        loadChart();
    });

});
