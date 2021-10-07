# bloxone custom list!

This will allow you to take any  **Domain Threat Intelligence** and import it in to @Infoblox Threat Defense Product


# What's needed

 - Python 3.6 or greater
 - Infoblox Bloxone module - https://pypi.org/project/bloxone/
 - Infoblox CSP API Token - https://csp.infoblox.com
	 - Please **DO NOT COPY THE API KEY FROM THE UI** if you have to create a new API key

> pip install bloxone

Edit csp.ini with Your API Token

> [BloxOne]
> url = 'https://csp.infoblox.com'
> 
> api_version = 'v1'
> 
> api_key = 'YOUR_TOKEN'

Then run "python3 get_insights.py"
