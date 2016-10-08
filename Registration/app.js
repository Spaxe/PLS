var express = require("express");
var bodyParser = require('body-parser');
var app = express();
var xhr = require("node-xhr");

// for parsing application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: true }));

app.use('/topup', express.static('app/public'));

app.post('/pay', function (req, res) {

  var token = '9135280005375941';
  var merchant = 'TESTHACK02';
  var order = 'order' + Math.round(Math.random() * 1000000);
  var transaction = 'transaction' + Math.round(Math.random() * 1000000);

  xhr.put({
    url: 'https://test-gateway.mastercard.com/api/rest/version/39/merchant/' + merchant + '/order/' + order + '/transaction/' + transaction,
    headers: {
      Authorization: 'Basic bWVyY2hhbnQuVEVTVEhBQ0swMjplODJjZDE1Y2ZjMDQwODUzMjNiN2UwYzYxNzAxODlmNw==',
    },
    body: {
      "apiOperation": "PAY",
      "order": {
        "amount": req.body.amount,
        "currency": "AUD"
      },
      "sourceOfFunds": {
        "token": token,
        "type": "CARD"
      }
    }
  }, function (error, resp) {
    if (error) {
      res.send(error);
      return;
    }

    res.send(resp);
  });

});

app.listen(8888, function () {
  console.log('Starting Server...');
});
