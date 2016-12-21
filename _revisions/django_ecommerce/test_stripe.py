import stripe
stripe.api_key = "sk_test_BQokikJOvBiI2HlWgH4olfQ2"
stripe.api_base = "https://api-tls12.stripe.com"

if stripe.VERSION in ("1.13.0", "1.14.0", "1.14.1", "1.15.1", "1.16.0", "1.17.0", "1.18.0", "1.19.0"):
  print("Bindings update required.")

try:
  stripe.Charge.all()
  print("TLS 1.2 supported, no action required.")
except stripe.error.APIConnectionError:
  print("TLS 1.2 is not supported. You will need to upgrade your integration.")
