/*This is where the major payment comes from

CSS emits from here:
https://stripe.com/docs/stripe-js

*/

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

//this is no longer present in the Stripe website, so I copied it from The lesson
var style = {
    base: {
        color: '#32325d',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#fa755a',
        iconColor: '#fa755a'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

// This will handle the error in the error
card.addEventListener('change', function (event) {
    var errorDiff = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiff).html(html);
    } else {
        errorDiff.textContent = '';
    }
});

// Handle form submit. Note that this is no longer in the Stripe website sot it is gotten from the lesson.
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    $('payment-form').fadeToggle(100);
    $('loading-innerclap').fadeToggle(100);

    var saveDetail = Boolean($('#id-save-info').attr('checked'));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postInfo = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_detail': saveDetail,
    }
    var url = '/checkout/stripe_checkout_data/';

    //This are the address details. Please note that these are Stripe in built details
    // This means they can not be altered or changed
    $.post(url, postInfo).done(function() {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.Name.value),
                    email: $.trim(form.email.value),
                    phone: $.trim(form.phone_number.value),
                    address:{
                        line1: $.trim(form.home_Address.value),
                        line2: $.trim(form.home_Address_continued.value),
                        country: $.trim(form.county.value),
                        state: $.trim(form.country.value),
                    }
            }
        },
        shipping: {
            name: $.trim(form.Name.value),
            phone: $.trim(form.phone_number.value),
            address:{
                line1: $.trim(form.home_Address.value),
                line2: $.trim(form.home_Address_continued.value),
                postal_code: $.trim(form.postcode.value),
                city: $.trim(form.county.value),
                country: $.trim(form.country.value),
            }
        },
        }).then(function(result) {
            if (result.error) {
                var errorDiff = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiff).html(html);
                $('payment-form').fadeToggle(100);
                $('loading-innerclap').fadeToggle(100);
                card.update({ 'disabled': false});
                $('#submit-button').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function () {
        location.reload();
    })
});