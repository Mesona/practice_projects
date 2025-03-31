// https://leetcode.com/problems/validate-ip-address/submissions/

/**
 * @param {string} IP
 * @return {string}
 */
var validIPAddress = function(IP) {
    let result = "Neither"
    if (IP.includes('.')) {
        let ip = IP.split('.');
        let ipReplace = IP.replace(/[0-9]/g, '')
        result = "IPv4";
        for (i = 0; i < ip.length; i++) {
            if (ip[i] < 0 || ip[i] > 255 || ip[i] === '') {
                result = "Neither";
            } else if (ip.length !== 4) {
                result = "Neither";
            } else if (ip[i][0] === '0' && ip[i].length !== 1) {
                result = "Neither";
            } else if (ip[i].includes('e')) {
                result = "Neither";
            } else if (ipReplace !== '...') {
                result = "Neither";
            }
        }
    } else if (IP.includes(':')) {
        let ip = IP.split(':');
        let ipReplace = IP.replace(/[0-9]/g, '').replace(/[a-f]/g, '').replace(/[A-F]/g, '')
        result = "IPv6";
        for (i = 0; i < 8; i++) {
            if (parseInt(ip[i], 16) > 65535 || ip[i] === '') {
                result = "Neither";
            } else if (ip.length !== 8) {
                result = "Neither";
            } else if (ip[i].length > 4) {
                result = "Neither";
            } else if (ip[i].match(/[g-z]/i) !== null) {
                result = "Neither";
            } else if (ipReplace !== ':::::::') {
                result = "Neither";
            }
        }
        
    }
    
    return result;
    
};
