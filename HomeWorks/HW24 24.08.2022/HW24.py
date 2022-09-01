request_from_user1 = {
    "url": "localhost/home/",
    "method": "GET",
    "data": {"попытка входа": 1},
    "timeout": 3000,
    "headers": {
        "Authorization": 'Bearer admin qwerty12345',
    },
}

request_from_user2 = {
    "url": "localhost/",
    "method": "POST",
    "data": {"попытка входа": 1},
    "timeout": 3000,
    "headers": {},
}


class AuthError(Exception):
    def __init__(self, exception_txt: str):
        self.exception_txt = exception_txt

    def print_error(self):
        print(f"ERROR: {self.exception_txt}!")


class RequestManager:
    def __init__(self, class_dict: dict):
        self.url = class_dict.get("url")
        self.method = class_dict.get("method")
        self.data = class_dict.get("data")
        self.timeout = class_dict.get("timeout")
        self.headers = class_dict.get("headers")

    def get_url(self):
        print(f"URL = {self.url}")
        return self.url

    def get_method(self):
        print(f"Method = {self.method}")
        return self.method


def measure(func):
    def wrap(dict_func: dict):
        # print('start measure')
        res = 0
        try:
            if len(dict_func["headers"]) != 0:
                res = RequestManager(dict_func)
                func(dict_func)
            else:
                raise AuthError("You give empty dict!")
        except AuthError as ae:
            ae.print_error()
        # print('end measure')
        return res

    return wrap


@measure
def print_dict(dict_func: dict):
    print(dict_func)


class HelpPython:
    PI = 3.141594

    @staticmethod
    def get_type_of_val(val):
        return type(val)

    @staticmethod
    def get_len_of_val(val):
        return len(val)

    @staticmethod
    def get_sum_of_val(a1: float, a2: float):
        return (a1 + a2)


if __name__ == '__main__':
    print_dict(request_from_user1)
