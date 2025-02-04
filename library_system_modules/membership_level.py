from enum import Enum

class MembershipLevel(Enum):
    BASIC = 100
    PREMIUM = 200
    GOLD = 500
    
    def get_annual_fee(self):
        return self.value