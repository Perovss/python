class VKuser:
    url = "https://api.vk.com/method/"

    def __init__(self, token, version):
        self.params = {
            'access_token': token,
            'v': version
        }

