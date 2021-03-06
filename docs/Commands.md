<!-- WARNING! This file is automatically generated, do not change it manually -->

**about**: Get information about the bot \
    Example: !about

**addalias**: Add alias for commands \
    Usage: !addalias &lt;command&gt; &lt;alias&gt; \
    Example: !addalias ping pong

**addbgevent**: Add background event \
    Example: !addbgevent 60 ping

**addcmd**: Add command \
    Example: !addcmd hello Hello!

**addextcmd**: Add command that executes external process \
    Note: Be careful when you are executing external commands! \
    Example: !addextcmd uname uname -a

**addimg**: Add image for !img command \
    Example: !addimg name url

**addmarkovfilter**: Add regular expression filter for Markov model \
    Example: !addmarkovfilter regex

**addquote**: Add quote to quotes database \
    Example: !addquote Hello, world!

**addreaction**: Add reaction \
    Example: !addreaction emoji regex

**addreminder**: Print message at particular time \
    Examples: \
        !addreminder 2020-01-01 00:00 Happy new year! \
        !addreminder today 08:00 Wake up \
        !addreminder tomorrow 08:00 Wake up \
        !addreminder 2d 08:00 Wake up &lt;- 2 days \
        !addreminder 1w 08:00 Wake up &lt;- 1 week \
        !addreminder in 1w5d10h5m Test reminder \
        !addreminder in 1w Test reminder 2 \
        !addreminder in 5h10m Test reminder 3 \


**addresponse**: Add bot response on message that contains particular regex \
    Example: !addresponse regex;text

**avatar**: Change bot avatar \
    Example: !avatar &lt;image&gt; \
    Hint: Use !listimg for list of available images

**channelid**: Get channel ID \
    Example: !channelid \
    *This command can be used as subcommand*

**config**: Setup some channel specific configurations \
    Examples: \
        !config reactions &lt;enable/disable&gt; \
        !config markovlog &lt;enable/disable&gt; \
        !config responses &lt;enable/disable&gt; \
        !config markovresponses &lt;enable/disable&gt; \
        !config markovpings &lt;enable/disable&gt;

**countchars**: Calculate length of the message \
    Example: !countchars some text \
    *This command can be used as subcommand*

**countlines**: Count amount of lines \
    Example: !count some text \
    *This command can be used as subcommand*

**countwords**: Count amount of words \
    Example: !count some text \
    *This command can be used as subcommand*

**curl**: Perform HTTP request \
    Usage: !curl &lt;url&gt; \
    *This command can be used as subcommand*

**delalias**: Delete command alias \
    Usage: !delalias &lt;alias&gt; \
    Example: !delalias pong

**delbgevent**: Delete background event \
    Example: !delbgevent 0

**delcmd**: Delete command \
    Example: !delcmd hello

**delimg**: Delete image for !img command \
    Example: !delimg name

**delmarkov**: Delete all words in Markov model by regex \
    Example: !delmarkov hello

**delmarkovfilter**: Delete regular expression filter for Markov model by index \
    Example: !delmarkovfilter 0 \
    *This command can be used as subcommand*

**delquote**: Delete quote from quotes database by index \
    Example: !delquote 0

**delreaction**: Delete reaction \
    Examples: \
        !delreaction index

**delreminder**: Delete reminder by index \
    Example: !delreminder 0

**delresponse**: Delete response \
    Examples: \
        !delresponse index

**demojify**: Demojify text \
    Example: !demojify 🇭 🇪 🇱 🇱 🇴 \
    *This command can be used as subcommand*

**disablecmd**: Disable command in specified scope \
    Examples: \
        !disablecmd ping \
        !disablecmd ping channel \
        !disablecmd ping guild \
        !disablecmd ping global

**dropmarkov**: Drop Markov database \
    Example: !dropmarkov

**emojify**: Emojify text \
    Example: !emojify Hello! \
    *This command can be used as subcommand*

**enablecmd**: Enable command in specified scope \
    Examples: \
        !enablecmd ping \
        !enablecmd ping channel \
        !enablecmd ping guild \
        !enablecmd ping global

**extexec**: Execute external shell command \
    Note: Be careful when you are executing external commands! \
    Example: !extexec uname -a \
    *This command can be used as subcommand*

**findmarkov**: Match words in Markov model using regex \
    Examples: \
        !findmarkov hello \
        !findmarkov hello -f

**help**: Print list of commands and get examples \
    Examples: \
        !help \
        !help -p \
        !help help

**img**: Send image (use !listimg for list of available images) \
    Example: !img &lt;image_name&gt;

**inspectmarkov**: Inspect next words in Markov model for current one \
    Example: !inspectmarkov hello

**listalias**: Print list of aliases \
    Example: !listalias \
    *This command can be used as subcommand*

**listbgevent**: Print list of background events \
    Example: !listbgevent \
    *This command can be used as subcommand*

**listimg**: Print list of available images for !img command \
    Example: !listimg

**listmarkovfilter**: Print list of regular expression filters for Markov model \
    Example: !listmarkovfilter \
    *This command can be used as subcommand*

**listquote**: Print list of all quotes \
    Example: !listquote

**listreaction**: Print list of reactions \
    Example: !listreaction \
    *This command can be used as subcommand*

**listreminder**: Print list of reminders \
    Example: !listreminder \
    *This command can be used as subcommand*

**listresponse**: Print list of responses \
    Example: !listresponse \
    *This command can be used as subcommand*

**markov**: Generate message using Markov chain \
    Example: !markov \
    *This command can be used as subcommand*

**markovgc**: Garbage collect Markov model nodes \
    Example: !markovgc

**message**: Get message by its order number (from the end of channel history) \
    Example: !message \
    *This command can be used as subcommand*

**permcmd**: Set commands permission \
    Example: !permcmd ping 0

**permuser**: Set user permission \
    Example: !permuser @nickname 0

**pin**: Print pinned message by its index \
    Example: !pin 0 \
    *This command can be used as subcommand*

**ping**: Check whether the bot is active and get latency in ms \
    Example: !ping

**poll**: Create poll \
    Example: !poll 60 option 1;option 2;option 3

**profile**: Print information about user \
    Examples: \
        !profile \
        !profile `@user`

**quote**: Print some quote from quotes database \
    Examples: \
        !quote \
        !quote 1

**random**: Get random number in range [left, right] \
    Example: !random 5 10 \
    *This command can be used as subcommand*

**randselect**: Get random option among provided strings (split by space) \
    Example: !randselect a b c \
    *This command can be used as subcommand*

**randselects**: Get random option among provided strings (split by semicolon) \
    Example: !randselects a;b;c \
    *This command can be used as subcommand*

**range**: Generate range of numbers \
    Examples: \
        !range &lt;stop&gt; \
        !range &lt;start&gt; &lt;stop&gt; \
        !range &lt;start&gt; &lt;stop&gt; &lt;step&gt; \
    *This command can be used as subcommand*

**remindme**: Ask bot to ping you when it sends reminder \
    Example: !remindme 1

**remindwme**: Ask bot to send direct message you when it sends reminder \
    Example: !remindwme 1

**repeatreminder**: Make reminder repeating with particular period \
    Examples: \
        !repeatreminder 1 1 \
        !repeatreminder 1 1h \
        !repeatreminder 1 1d \
        !repeatreminder 1 1w \
    Note: number without postfix is translated to minutes

**restart**: Restart the bot \
    Example: !restart

**server**: Print information about current server \
    Example: !server

**setquoteauthor**: Set author of quote by its index \
    Example: !setquoteauthor 0 WalBot

**shutdown**: Shutdown the bot \
    Example: !shutdown

**silent**: Make the following command silent (without any output to the chat) \
    Example: !silent ping

**skipreminder**: Skip next instance of recurring (repeating) reminder \
    Example: !skipreminder 1 \
    Note: only recurring (repeating) reminders are affected by this command

**slowmode**: Edit slowmode \
    Example: !slowmode 0

**statmarkov**: Show stats for Markov module \
    Example: !statmarkov

**status**: Change bot status \
    Examples: \
        !status idle \
        !status playing Dota 2 \
    Possible activities: [playing, streaming, watching, listening] \
    Possible bot statuses: [online, idle, dnd, invisible]

**takechars**: Take n characters of the string \
    Examples: \
        !takechars 2 hello \
        Result: he \
        !takechars -2 hello \
        Result: lo \
    *This command can be used as subcommand*

**takelines**: Take n lines of the string \
    Examples: \
        !takelines 2 a \
        b \
        c \
        Result: a \
        b \
        !takelines -2 a \
        b \
        c \
        Result: b \
        c \
    *This command can be used as subcommand*

**takewords**: Take n words of the string \
    Examples: \
        !takewords 2 a b c \
        Result: a b \
        !takewords -2 a b c \
        Result: b c \
    *This command can be used as subcommand*

**time**: Show current time \
    Example: !time \
    *This command can be used as subcommand*

**timescmd**: Print how many times command was invoked \
    Examples: \
        !timescmd echo \
        !timescmd echo -s \
    *This command can be used as subcommand*

**tolower**: Convert text to lower case \
    Example: !tolower SoMe TeXt \
    *This command can be used as subcommand*

**toupper**: Convert text to upper case \
    Example: !toupper SoMe TeXt \
    *This command can be used as subcommand*

**tts**: Send text-to-speech (TTS) message \
    Example: !tts Hello!

**updcmd**: Update command (works only for commands that already exist) \
    Example: !updcmd hello Hello!

**updextcmd**: Update command that executes external process (works only for commands that already exist) \
    Note: Be careful when you are executing external commands! \
    Example: !updextcmd uname uname -a

**updreaction**: Update reaction \
    Example: !updreaction index emoji regex

**updreminder**: Update reminder by index \
    Example: !updreminder 0 2020-01-01 00:00 Happy new year!

**updresponse**: Update bot response \
    Example: !updresponse index regex;text

**uptime**: Show bot uptime \
    Example: !uptime \
    *This command can be used as subcommand*

**urlencode**: Urlencode string \
    Example: !urlencode hello, world! \
    *This command can be used as subcommand*

**version**: Get version of the bot \
    Examples: \
        !version \
        !version short \
    *This command can be used as subcommand*

**whitelist**: Bot's whitelist \
    Examples: \
        !whitelist enable/disable \
        !whitelist add \
        !whitelist remove

**wme**: Send direct message to author with something \
    Example: !wme Hello!

**wmeimg**: Send image in direct message to author \
    Example: !wmeimg &lt;image_name&gt;
