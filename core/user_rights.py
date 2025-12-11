from core.windows_secedit import SeceditModule

class UserRightsModule(SeceditModule):
    def apply_user_right(self, privilege_constant, desired_users_list):
        # Convert python list to secedit comma string
        # If list is empty, secedit uses empty string to denote "No One"
        target_val = ",".join(desired_users_list)
        
        # Apply using the generic secedit logic
        # Note: secedit expects values to look like: SeDebugPrivilege = *S-1-5-32-544,Administrator
        self.apply_secedit_policy(privilege_constant, target_val, section_name="Privilege Rights")