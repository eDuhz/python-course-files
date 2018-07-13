import webbrowser

#webbrowser.open()

help(webbrowser)
"""Dunno why this don't work hahahaha"""
#chrome = webbrowser.get(using= 'google-chrome')
#chrome.open_new('https://www.python.org')
windowsDef = webbrowser.get(using='windows-default')

windowsDef.open_new("https://www.python.org")