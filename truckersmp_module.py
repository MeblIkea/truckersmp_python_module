import requests


class get_user:
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.response = requests.get(f'https://api.truckersmp.com/v2/player/{user_id}').json().get('response')

    def name(self):
        return self.response.get('name')

    def id(self):
        return {'id': self.response.get('id'), 'steamID64': self.response.get('steamID64'),
                'steamID': self.response.get('steamID')}

    def avatar_url(self, small=False):
        if small:
            return self.response.get('smallAvatar')
        else:
            return self.response.get('avatar')

    def join_at(self):
        date = self.response.get('joinDate')
        return {'date': date.split(' ')[0], 'hour': date.split(' ')[1]}

    def is_banned(self):
        return self.response.get('banned')

    def get_bans(self):
        if self.response.get('displayBans'):
            return requests.get(f'https://api.truckersmp.com/v2/bans/{self.user_id}').json().get('response')
        else:
            return 'Bans hidden'

    def is_patreon(self):
        if self.response.get('patreon').get('isPatron'):
            return self.response.get('patreon')
        else:
            return False

    def permissions(self):
        perm = "user"
        if self.response.get('permissions').get('isStaff'):
            perm = 'staff'
        if self.response.get('permissions').get('isUpperStaff'):
            perm = 'upper_staff'
        if self.response.get('permissions').get('isGameAdmin'):
            perm = 'game_admin'
        return perm


class get_vtc:
    def __init__(self, vtx_id: int):
        self.response = requests.get(f'https://api.truckersmp.com/v2/vtc/{vtx_id}').json().get('response')

    def id(self):
        return self.response.get('id')

    def name(self):
        return self.response.get('name')

    def get_owner(self):
        return {'owner_id': self.response.get('owner_id'), 'owner_username': self.response.get('owner_username')}

    def slogan(self):
        return self.response.get('slogan')

    def tag(self):
        return self.response.get('tag')

    def pictures(self):
        return [self.response.get('logo'), self.response.get('cover')]

    def information(self):
        return {'information': self.response.get('information'), 'rules': self.response.get('rules'),
                'requirements': self.response.get('requirements'), 'is_recruiting': self.response.get('recruitment'),
                'website': self.response.get('website')}

    def social_network(self):
        return self.response.get('socials')

    def language(self):
        return self.response.get('language')

    def is_verified(self):
        return self.response.get('verified')

    def created_at(self):
        date = self.response.get('created')
        return {'date': date.split(' ')[0], 'hour': date.split(' ')[1]}

    def games(self):
        return {'ets2': self.response.get('games').get('ets'), 'ats': self.response.get('games').get('ats')}

    def members(self):
        member = requests.get(f'https://api.truckersmp.com/v2/vtc/{self.id()}/members').json().get('response')\
            .get('members')
        return {'count': self.response.get('members_count'), 'list': member}

    def roles(self):
        role = requests.get(f'https://api.truckersmp.com/v2/vtc/{self.id()}/roles').json().get('response')\
            .get('roles')
        return {'count': len(role), 'list': role}


class get_server:
    def __init__(self):
        self.response = requests.get('https://api.truckersmp.com/v2/version').json()

    def version(self):
        self.response.get('name')

    def time(self):
        date = self.response.get('created')
        return {'date': date.split(' ')[0], 'hour': date.split(' ')[1]}

    def supported_games_version(self):
        return {'ets2': self.response.get('supported_game_version'),
                'ats': self.response.get('supported_ats_game_version')}

    def servers(self, server_name: str = None):
        self.response = requests.get('https://api.truckersmp.com/v2/servers').json().get('response')
        if server_name is None:
            servers = {}
            for x in self.response:
                servers[x.get('id')] = x.get('name')
            return servers
        else:
            for x in self.response:
                if x.get('name') == server_name:
                    return x
            return 'Server not found.'
