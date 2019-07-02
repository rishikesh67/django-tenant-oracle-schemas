### No cross domain cookie is possible (with no .com or any domain)

nseinvestese:9000
cfd.nseinvestease:9000
nm2.nseinvestease:9000


### .com domain (cross domain cookie is possible)

nseinvestese.com:9000
cfd.nseinvestease.com:9000
nm2.nseinvestease.com:9000

### Solution 1 - Pass token through url bar

+ Once login is successful, a token will be issued in main domain that needs to be transferred to the subdomain through Url bar, in this case, setting HTTP-Only cookie is not possible because that will not allow us to access the cookie value using JS code.

+ It looks like a security concern but JWT are mostly safe if they are signed with a hard to guess sign key. But still we don't want to reveal this as well then this approach is not a right choice.

### Solution 2 - Add `.com` extension to the main domain

`nseinvestease` > `nseinvestease.com`

So that tenant would look like

`nseinvestese.com:9000` > `cfd.nseinvestease.com:9000`

`nmf2.nseinvestese.com:9000` > `nmf2.nseinvestease.com:9000`

