var xhr = require('xhr');

var pay = document.getElementById('pay');
var receipt = document.getElementById('receipt');
var account_balance = document.getElementById('account-balance');

var balance = 35;

pay.addEventListener('click', () => {

  var amount = document.getElementById('amount');
  xhr.post({
    url: '/pay',
    timeout: 35000,
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: 'amount=' + amount.value
  }, (error, resp, body) => {
    if (error) {
      console.log(error);
      return;
    }

    let json = JSON.parse(body);

    let response = json.body.response.acquirerCode;
    if (response !== '00') {
      console.log(json.body.response);
      receipt.textContent = "We're sorry, your card was denied. Please try another card.";
      return;
    }

    let paid = json.body.transaction.amount;
    balance += paid;
    let paid_display = Number(paid).toFixed(2);
    let balance_display = Number(balance).toFixed(2);
    account_balance.textContent = `$${balance_display}`;

    receipt.innerHTML = `
      <h1>Payment Successful</h1>
      <p>Amount: $${paid_display}</p>
      <p>New Balance: $${balance_display}</p>
      <p>Card: ${json.body.sourceOfFunds.provided.card.number}</p>
      <p>${json.body.sourceOfFunds.provided.card.scheme} issued by ${json.body.sourceOfFunds.provided.card.issuer}</p>
      <p>Reference Number: ${json.body.order.id}</p>
    `;
  });
});
