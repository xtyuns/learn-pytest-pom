class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.get_by_label("帐号")
        self.password_input = page.get_by_label("密码", exact=True)
        self.login_button = page.get_by_role("button", name="登 录")

    def navigate(self):
        self.page.goto("/login")

    def input_username(self, username):
        self.username_input.fill(username)

    def input_password(self, password):
        self.password_input.fill(password)

    def login(self):
        self.login_button.click()
