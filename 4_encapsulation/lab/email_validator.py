import re


class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def validate(self, tokens):
        (name, mail, domain) = re.split(r"[@.]", tokens)
        return self.__validate_name(name) and \
               self.__validate_mail(mail) and \
               self.__validate_domain(domain)

    def __validate_name(self, name):
        return self.min_length <= len(name)

    def __validate_mail(self, mail):
        return mail in self.mails

    def __validate_domain(self, domain):
        return domain in self.domains


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
