
$(document).ready(function () {
    $(document).on('click', '.payWithRazorpay', function (e) {
        e.preventDefault();

        var fname = $("[name='fname']").val();
        var lname = $("[name='lname']").val();
        var email = $("[name='email']").val();
        var phone = $("[name='phone']").val();
        var address = $("[name='address']").val();
        var city = $("[name='city']").val();
        var state = $("[name='state']").val();
        var country = $("[name='country']").val();
        var pincode = $("[name='pincode']").val();
        var token = $("[name='csrfmiddlewaretoken']").val();

        if (!fname || !lname || !email || !phone || !address || !city || !state || !country || !pincode) {
            swal("Alert!", "Enter all fields!", "error");
            return false;
        }

        $.ajax({
            method: "GET",
            url: "/proceedtopay",
            success: function (response) {
                var options = {
                    "key": "rzp_test_Pc1nK7R22J5sMy",
                    "amount": response.total_price * 100,
                    "currency": "INR",
                    "name": "ShopSphere",
                    "description": "Thank you for choosing us!",
                    "handler": function (responseb) {
                        var data = {
                            "fname": fname,
                            "lname": lname,
                            "email": email,
                            "phone": phone,
                            "address": address,
                            "city": city,
                            "state": state,
                            "country": country,
                            "pincode": pincode,
                            "payment_mode": "Paid by Razorpay",
                            "payment_id": responseb.razorpay_payment_id,
                            "csrfmiddlewaretoken": token
                        };

                        $.ajax({
                            method: "POST",
                            url: "/placeorder",
                            data: data,
                            success: function (responsec) {
                                swal("Congratulations!", responsec.status, "success").then(() => {
                                    window.location.href = '/myorders';
                                });
                            },
                            error: function () {
                                swal("Error!", "Order placement failed.", "error");
                            }
                        });
                    },
                    "prefill": {
                        "name": fname + " " + lname,
                        "email": email,
                        "contact": phone
                    },
                    "theme": {
                        "color": "#3399cc"
                    }
                };
                var rzp1 = new Razorpay(options);
                rzp1.open();
            },
            error: function () {
                swal("Error!", "Could not proceed to payment.", "error");
            }
        });
    });
});
