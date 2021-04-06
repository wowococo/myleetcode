from leezy import solution, Solution


class Q468(Solution):
    @solution
    def validIPAddress(self, IP):
        if self.validIPv4(IP):
            return "IPv4"
        elif self.validIPv6(IP):
            return "IPv6"
        else:
            return "Neither"
    
    def validIPv4(self, IP):
        parts = IP.split('.')
        if len(parts) != 4:
            return False
        for part in parts:
            print(part)
            if not part:
                return False
            if len(part) > 1 and part[0] == '0':
                return False
            for ch in part:
                if not ch.isdigit():
                    return False
                
            if int(part) > 255:
                return False
            
        return True    
        
    def validIPv6(self, IP):
        """
        A-F 65-70
        a-f 97-102
        多余的 0 不被允许说的是不能使 ipv6 地址的单个部分超过四位十六进制
        02001:0db8:85a3:0000:0000:8a2e:0370:7334 是无效的
        2001:0db8:85a3:0000:0000:8a2e:0370:7334 是"IPv6"，中间部分的这种四个 0 是允许的
        """
        parts = IP.split(':')
        if len(parts) != 8:
            return False
        for part in parts:
            if len(part) > 4 or len(part) < 1:
                return False
            for ch in part:
                if not ch.isdigit():
                    if not ((ord('A') <= ord(ch) <= ord('F')) or (ord('a') <= ord(ch) <= ord('f'))):
                        return False
        return True


def main():
    q = Q468()
    q.add_case(q.case('172.16.254.1').assert_equal("IPv4"))
    q.add_case(q.case("2001:0db8:85a3:0:0:8A2E:0370:7334").assert_equal('IPv6'))
    q.add_case(q.case("256.256.256.256").assert_equal("Neither"))
    q.add_case(q.case("2001:0db8:85a3:0:0:8A2E:0370:7334:").assert_equal("Neither"))
    q.add_case(q.case("1e1.4.5.6").assert_equal("Neither"))
    q.add_case(q.case("01.01.01.01").assert_equal('Neither'))
    q.add_case(q.case("2001:0db8:85a3:0000:0000:8a2e:0370:7334").assert_equal('IPv6'))
    q.add_case(q.case("02001:0db8:85a3:0000:0000:8a2e:0370:7334").assert_equal('Neither'))

    q.run()


if __name__ == '__main__':
    main()
