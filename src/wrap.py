import abc

import discord

from .config import bc


class WbWrapper(abc.ABC):
    def __repr__(self) -> str:
        return repr(self.__dict__)


class WbGuild(WbWrapper):
    def __init__(self, guild: discord.Guild) -> None:
        self.id = guild.id
        self.name = guild.name
        self.member_count = guild.member_count
        self.region = guild.region
        self.created_at = guild.created_at
        self.icon_url = guild.icon_url
        self.owner_id = guild.owner_id

    @property
    def _guild(self):
        return bc.get_guild(self.id)

    def fetch_members(self, *args, **kwargs):
        return self._guild.fetch_members(*args, **kwargs)

    def get_member(self, *args, **kwargs):
        return self._guild.get_member(*args, **kwargs)


class WbMember(WbWrapper):
    def __init__(self, member: discord.Member) -> None:
        self.id = member.id
        self.name = member.name
        self.discriminator = member.discriminator
        self.bot = member.bot
        self.nick = member.nick
        self.guild = WbGuild(member.guild)

    @property
    def mention(self):
        return f'<@{self.id}>'

    def __str__(self) -> str:
        return f"{self.name}#{self.discriminator}"


class WbTextChannel(WbWrapper):
    def __init__(self, channel: discord.TextChannel):
        self.id = channel.id
        self.name = channel.name
        self.position = channel.position
        self.nsfw = channel.nsfw
        self.category_id = channel.category_id
        self.guild = WbGuild(channel.guild)

    @property
    def _channel(self):
        return bc.get_channel(self.id)

    def send(self, *args, **kwargs):
        return self._channel.send(*args, **kwargs)

    def fetch_message(self, *args, **kwargs):
        return self._channel.fetch_message(*args, **kwargs)


class WbMessage(WbWrapper):
    def __init__(self, message: discord.Message) -> None:
        self.id = message.id
        self.content = message.content
        self.author = WbMember(message.author)
        self.channel = WbTextChannel(message.channel)
        self.guild = WbGuild(message.guild)
