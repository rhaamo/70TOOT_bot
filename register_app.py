#!/usr/bin/env python3

import os
import config
from mastodon import Mastodon

if not os.path.exists('bot.clientcred.secret'):
    Mastodon.create_app(
        '74LS7007bot',
        api_base_url = config.url,
        to_file = 'bot.clientcred.secret'
    )
    mastodon = Mastodon(
        client_id = 'bot.clientcred.secret',
        api_base_url = config.url
    )
    mastodon.log_in(
        config.email,
        config.password,
        to_file = 'bot.usercred.secret'
    )
