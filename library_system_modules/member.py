from library_system_modules.membership_level import MembershipLevel
from library_system_modules.library_exceptions import InvalidMembershipError

class Member:
    def __init__(self, name: str, membership_level: MembershipLevel):
        self.name = name
        if not isinstance(membership_level, MembershipLevel):
            raise InvalidMembershipError(membership_level)
        self.membership_level = membership_level

    def get_fee(self):
        if not isinstance(self.membership_level, MembershipLevel):
            raise InvalidMembershipError(self.membership_level)
        return self.membership_level.get_annual_fee()