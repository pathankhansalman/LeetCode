class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique_emails = []
        for email in emails:
            at_pos = email.find("@")
            prefix = email[:at_pos]
            domain = email[at_pos+1:]
            if "+" in prefix:
                plus_pos = prefix.find("+")
                prefix = prefix[:plus_pos]
            prefix = prefix.replace(".", "")
            unique_emails.append(prefix + "@" + domain)
        return len(set(unique_emails))