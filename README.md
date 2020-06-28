# Access Point Checker

This Python program is used to check access points around a property. It is able to be set and scheduled to run at a specific time, alerting the admin only when some port is not down.

## Installation

1. Download the program from Github. (Click "Clone" at the top right and then "Download ZIP", then unpack the ZIP)
2. Set up the list of locations in `locations.txt`. See below for how to do this.
3. Provide your Sendgrid API key (which allows the bot to send emails on an access port going down). See below on how to configure the `.env` file below.
4. Install the necessary Python packages. The following commands can be run to do so: `py -m pip install -r requirements.txt`
5. Configure `settings.py` to include the from/to emails. See more on this below.
6. Run/schedule the `ping.py` file.

## Configuring `locations.txt`

These are currently four properties to each location:
1. IP ending (such as "96", where the location IP is `192.168.0.96`)
2. Location (such as "Main Lobby")
3. Whether the location is a Linksys router (which are ignored on default)
4. Whether the location should be manually ignored.

A location is represented in this file by one line in the following format:

`ending, location, linksys=True/False, ignore=True/False,`

Multiple locations are shown in this file by compiling these statements line-by-line. The commas at the end of the line should be there. An example is shown below.

```
10, "Lobby", linksys=True, ignore=False,
11, "Atrium", linksys=False, ignore=False,
12, "Main Restaurant", linksys=False, ignore=True,
```

## Configuring the `.env` file

To configure the `.env` file, simply add two things (the Sendgrid API Key and the beginning of the network IP). More information about finding your SendGrid API key can be found [here](https://sendgrid.com/docs/ui/account-and-settings/api-keys/). The `.env` file should look like:

```
SENDGRID_API_KEY='abcdefghijklmnopqrstuvwxyz'
IP_PRE='192.160.0.'
```

## Configuring the `settings.py` file

Part of this file is editable; part of the file is not. The editable part (below the multi-line comment) should be set up as follows:

```
FROM_EMAIL='example1@example.com'
TO_EMAIL='example2@example.com'
SUBJECT='Email Subject'
```