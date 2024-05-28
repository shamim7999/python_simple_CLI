class Account:
    def __init__(self, account_id, amount, account_type, date, reason, person_id):
        self.account_id = account_id
        self.amount = amount
        self.account_type = account_type
        self.date = date
        self.reason = reason
        self.person_id = person_id

    def __repr__(self):
        return (f"Account(id={self.account_id}, amount={self.amount}, type={self.account_type}, "
                f"date={self.date}, reason={self.reason}, person_id={self.person_id})")
