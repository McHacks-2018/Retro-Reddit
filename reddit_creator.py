#!/usr/bin/env python

"""This example demonstrates the flow for retrieving a refresh token.

In order for this example to work your application's redirect URI must be set
to http://localhost:8080.

This tool can be used to conveniently create refresh tokens for later use with
your web application OAuth2 credentials.

"""
import logging
import random
import socket
import sys
import conf
import webbrowser
import praw

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logger = logging.getLogger('retroreddit-creator')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)


def receive_connection():
    """Wait for and then return a connected socket..

    Opens a TCP connection on port 8080, and waits for a single client.

    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('localhost', 8080))
    server.listen(1)
    client = server.accept()[0]
    server.close()
    return client


def send_message(client, message):
    """Send message to client and close the connection."""
    print(message)
    client.send('HTTP/1.1 200 OK\r\n\r\n{}'.format(message).encode('utf-8'))
    client.close()


def request_login(reddit):
    """Provide the program's entry point when directly executed."""
    scopes = ['edit', 'history', 'identity',
              'mysubreddits', 'privatemessages', 'read', 'report',
              'save', 'submit', 'subscribe', 'vote']
    # scopes = ['creddits', 'edit', 'flair', 'history', 'identity',
    #           'modconfig', 'modcontributors', 'modflair', 'modlog',
    #           'modothers', 'modposts', 'modself', 'modwiki',
    #           'mysubreddits', 'privatemessages', 'read', 'report',
    #           'save', 'submit', 'subscribe', 'vote', 'wikiedit',
    #           'wikiread']

    state = str(random.randint(0, 65000))
    url = reddit.auth.url(scopes, state, 'permanent')
    webbrowser.open(url)
    sys.stdout.flush()

    client = receive_connection()
    data = client.recv(1024).decode('utf-8')
    param_tokens = data.split(' ', 2)[1].split('?', 1)[1].split('&')
    params = {key: value for (key, value) in [token.split('=')
                                              for token in param_tokens]}

    if state != params['state']:
        send_message(client, 'State mismatch. Expected: {} Received: {}'
                     .format(state, params['state']))
        return None
    elif 'error' in params:
        send_message(client, params['error'])
        return None

    refresh_token = reddit.auth.authorize(params['code'])
    send_message(client, 'Refresh token: {}; please close this window'.format(refresh_token))
    return refresh_token


def create_reddit(refresh_token=None):
    if isinstance(refresh_token, str) and refresh_token:
        reddit = praw.Reddit(client_id=conf.clientId,
                             client_secret=conf.clientSecret,
                             user_agent=conf.userAgent,
                             redirect_uri='http://localhost:8080',
                             refresh_token=refresh_token)
        reddit.config.decode_html_entities = False
        reddit.read_only = False
        return reddit
    reddit = praw.Reddit(client_id=conf.clientId,
                         client_secret=conf.clientSecret,
                         redirect_uri='http://localhost:8080',
                         user_agent=conf.userAgent)
    reddit.config.decode_html_entities = False
    return reddit


def init_reddit():
    try:
        with open("retro_reddit.txt", "r+") as token_file:
            token = token_file.readline()
            logger.debug("Init with token {}".format(token))
            if token:
                return create_reddit(token)
    except FileNotFoundError:
        pass
    return create_reddit()


def save_token(refresh_token):
    with open("retro_reddit.txt", "w+") as token_file:
        token_file.write(refresh_token)
        token_file.flush()


def login(reddit, refresh_token=None):
    if isinstance(refresh_token, str) and refresh_token:
        logger.debug("Found token {}".format(refresh_token))
        save_token(refresh_token)
        return create_reddit(refresh_token)
    logger.debug("Launching login request")
    token = request_login(reddit)
    if token is not None:
        save_token(token)
        return create_reddit(token)
    return reddit

