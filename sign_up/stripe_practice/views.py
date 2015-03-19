from flask import Blueprint, flash, render_template, request, redirect, jsonify
import requests
import stripe
import os
import json
import urllib
from flask import current_app as app

#will store in env variables after testing is over.



stripe_practice = Blueprint("stripe_practice", __name__)
#
@stripe_practice.route('/charge', methods=['POST'])
def charge():
    # Amount in cents
    amount = 500

    customer = stripe.Customer.create(
        email='customer@example.com',
        card=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Flask Charge'
    )

    return render_template('charge.html', amount=amount)


@stripe_practice.route('/')
def index():
  return render_template('index.html', key=app.config.get('publishable_key'))

@stripe_practice.route('/authorize')
def authorize():
  site  = 'https://connect.stripe.com' + '/oauth/authorize'
  params = {
             'response_type': 'code',
             'scope': 'read_write',
             'client_id': app.config.get('CLIENT_ID')
           }

  # Redirect to Stripe /oauth/authorize endpoint
  url = site + '?' + urllib.parse.urlencode(params)
  return redirect(url)

@stripe_practice.route('/oauth/callback')
def callback():
  code   = request.args.get('code')
  data   = {
             'client_secret': app.config.get('client_secret'),
             'grant_type': 'authorization_code',
             'client_id': app.config.get('CLIENT_ID'),
             'code': code
           }

  # Make /oauth/token endpoint POST request
  url = 'https://connect.stripe.com' + '/oauth/token'
  resp = requests.post(url, params=data)
  print(resp)
  resp = resp.json()
  token = resp['access_token']
  return render_template('callback.html', token=token)

if __name__ == '__main__':
  app.run(debug=True)
