# Helper function to check if a substring is a valid IP address segment
def isValidSegment(s):
    # Segment must not be empty, and must be between 0 and 255
    if len(s) == 0 or (len(s) > 1 and s[0] == '0') or int(s) > 255:
        return False
    return True


# Recursive function to restore IP addresses
def restoreIpAddresses(s, start, part, currentIP, result):
    # Base case: if we have filled 4 parts and used up all characters
    if part == 4 and start == len(s):
        # Remove trailing '.'
        result.append(currentIP[:-1])
        return

    # Exit if more parts are required or too few characters remain for valid segments
    if part == 4 or start == len(s):
        return

    length = 1
    # Try each segment length (1 to 3 digits)
    while length <= 3 and start + length <= len(s):
        segment = s[start:start + length]

        if isValidSegment(segment):
            restoreIpAddresses(s, start + length, part + 1, currentIP + segment + ".", result)
        length += 1


def generateIpAddresses(s):
    result = []
    restoreIpAddresses(s, 0, 0, "", result)
    return result


s = "25525511135"
validIPs = generateIpAddresses(s)

print("Valid IP addresses:")
for ip in validIPs:
    print(ip)


'''
Time Complexity: O(1), bounded by fixed IPv4 segment choices.

Reason:
An IP address always has exactly 4 parts, and each part can have
only 1 to 3 digits.
So the recursion tries a fixed maximum number of combinations,
not dependent on a large input size.

Space Complexity: O(1), excluding output.

Reason:
The recursion depth is at most 4 because there are only 4 IP parts.
The result list is output space.
'''
