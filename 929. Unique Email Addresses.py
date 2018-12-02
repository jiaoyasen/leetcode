class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        #my code
        str_set = set()
        for str_email in emails:
            localname, _, domainname = str_email.partition('@')
            name = localname.split('+')[0].replace('.', '') + '@' + domainname
            str_set.add(name)
        return len(str_set)
        #best code
        seen = set()  # unique strings
        for email in emails:
            # partition email into local and domain parts by "@" sign
            local, _, domain = email.partition("@")
            if '+' in local:
                local = local[:local.index('+')]
            seen.add(local.replace('.', '') + '@' + domain)
        return len(seen)